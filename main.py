import chainlit as cl  # Import Chainlit
from agents import Agent, Runner, trace
from connection import config
import asyncio

# --- Agent Definitions ---

# Poetry Agent - generates or processes poems
poetry_agent = Agent(
    name='Poetry Agent',
    instructions="""
        You are a poet agent. Your role is to generate a two-stanza poem or process an input poem.
        Poems can be lyric (emotional), narrative (storytelling), or dramatic (performance).
        If you're asked without a poem, generate a short two-stanza poem on emotions.

        IMPORTANT: You must write your poems in Roman Urdu.
        For example: "Chand ne poocha, kis ki talaash hai, aankhon ne sirf tera naam likha."
        If the user asks for a poem, generate it in Roman Urdu.
    """,
)

# Analyst Agents for different poetry types

lyric_analyst_agent = Agent(
    name="Lyric Analyst Agent",
    instructions="""
        You analyze lyric poetry focusing on emotions, feelings, and musicality.
        Provide insights about the poem's mood, use of rhythm, and personal voice.
        Your analysis should be in English.
        IMPORTANT: Be prepared to analyze poems in Roman Urdu, and understand keywords in Roman Urdu as well.
    """,
)

narrative_analyst_agent = Agent(
    name="Narrative Analyst Agent",
    instructions="""
        You analyze narrative poetry focusing on storytelling elements: plot, characters, and imagery.
        Your analysis should be in English.
        IMPORTANT: Be prepared to analyze poems in Roman Urdu, and understand keywords in Roman Urdu as well.
    """,
)

dramatic_analyst_agent = Agent(
    name="Dramatic Analyst Agent",
    instructions="""
        You analyze dramatic poetry emphasizing voice, dialogue, and performance aspects.
        Your analysis should be in English.
        IMPORTANT: Be prepared to analyze poems in Roman Urdu, and understand keywords in Roman Urdu as well.
    """,
)

# --- Custom Parent Agent with post-process logic ---

class CustomParentAgent(Agent):
    async def run(self, input, config):
        # Step 1: Generate or process poem
        poet_output = await poetry_agent.run(input, config)
        poem_text = poet_output.output.lower()

        # Step 2: Detect type
        if any(keyword in poem_text for keyword in ["dialogue", "voice", "stage", "guftagu", "aawaz"]):
            next_agent = dramatic_analyst_agent
        elif any(keyword in poem_text for keyword in ["story", "character", "event", "kahani", "kirdar"]):
            next_agent = narrative_analyst_agent
        else:
            next_agent = lyric_analyst_agent

        # Step 3: Analyze poem
        final_output = await next_agent.run(poet_output.output, config)
        return final_output

# --- Parent Agent Setup ---

parent_agent = CustomParentAgent(
    name="Parent Poet Orchestrator",
    instructions="""
        You are the orchestrator agent for poetry tasks.
        When given a request or poem, first delegate to the poet agent to generate or process poems.
        After receiving the poem, detect whether it's lyric, narrative, or dramatic poetry.
        Delegate the poem to the corresponding analyst agent for deeper analysis.
        If the type is unclear or multiple types apply, delegate to all analysts.
        If the query is unrelated to poetry, respond politely and do not delegate.

        All internal processes and orchestrator responses should be in English.
        However, if the user asks for a poem in Roman Urdu, the Poet Agent will handle that.
    """,
    handoffs=[poetry_agent, lyric_analyst_agent, narrative_analyst_agent, dramatic_analyst_agent]
)

# --- Chainlit UI Integration ---

@cl.on_chat_start
async def start():
    welcome_message = """
    **Welcome to the Poetry Agent!** 🎭
    """
    await cl.Message(content=welcome_message).send()

@cl.on_message
async def main_chainlit_runner(message: cl.Message):
    user_input = message.content

    await cl.Message(content="✍️ Writing your poem and analyzing it...").send()

    try:
        result = await Runner.run(
            parent_agent,
            user_input,
            run_config=config
        )

        final_output_message = f"**📜 Final Output:**\n\n{result.final_output}"
        #last_agent_message = f"**🔍 Analyzed by:** `{result.last_agent.name}`"

        await cl.Message(content=final_output_message).send()
        #await cl.Message(content=last_agent_message).send()

    except Exception as e:
        await cl.Message(content=f"❌ Error occurred: {str(e)}").send()
