import OpenAI from 'openai';
import { OpenAIStream, StreamingTextResponse } from 'ai';

const openai = new OpenAI({
  baseURL: "http://127.0.0.1:5000/v1",
});

export const runtime = 'edge';

export async function POST(req: Request) {
  const { messages } = await req.json();

  const response = await openai.chat.completions.create({
    model: 'gpt-3.5-turbo',
    stream: true,
    messages: [
      {
        role: "system",
        content:
          `You are a professional joke teller who has been hired to write a series of short jokes for young audience. The jokes should be captivating, imaginative, and humorous. They should explore a variety of topics, from work and people to animals, food, television, and so on. Each joke should be unique and memorable, with compelling humor and unexpected plot twists. Each joke should have no more than 50 English words.`,
      },
      {
        role: "system",
        content:
          `You are are also able evaluate a given joke. The joke is quoted in with triple qutation marks ("""). You should evaluate if the joke is funny or not, appropriated or not, offensive or not, and other criteria you might judge important`,
      },
      ...messages,
    ],
  });

  const stream = OpenAIStream(response);
  return new StreamingTextResponse(stream);
}