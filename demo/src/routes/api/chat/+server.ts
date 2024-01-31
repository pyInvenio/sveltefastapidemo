import { OPEN_AI_KEY } from '../../../lib/server/config';
import OpenAI from 'openai';

const openai = new OpenAI({apiKey: OPEN_AI_KEY});

export const POST = async ({request}) => {
    const text = await request.json();
    const query = text.query;

    const res = await openai.chat.completions.create({
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": query
            }
          ]
    });

    const answer = res["choices"][0]["message"]["content"];
    return new Response(JSON.stringify({answer}), { status: 200 });
};