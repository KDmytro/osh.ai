# osh.ai

Small business is the economic backbone of the country, yet it is difficult and time consuming to discover, understand, and comply with small business regulations. With the new breed of generative AI, people of small business, using their own plain natural language, can ask about relevant regulations, in a sense, they can “talk to the law”.  This demo is a proof of concept in a narrow scope, showing how langchain can vectorize specific sections of regulation and make it possible to elicit relevant context through a [simple App UI](https://www.youtube.com/watch?v=2fBmVCVRvAw) and let users pose questions and get actual drafts as a starting point to understanding their legal obligations. 

We believe this demonstrates the proof of concept, now imagine what's possible if anybody could just talk to law and regulation?

* **IMPACT:** Small Business is the economic backbone of the country
> 33.2 million small businesses According to the U.S. Small Business Association (SBA), small businesses of 500 employees or fewer make up 99.9% of all U.S. businesses and 99.7% of firms with paid employees.

* **PAIN:** Difficult and time consuming to discover, understand, and comply with small business regulations

* **SOLUTION:** With the new breed of generative AI, people of small business, using their own plain natural language, can ask about relevant regulations, in a sense, they can “talk to the law”

* **TECH:** This demo is a proof of concept in a narrow scope, showing how langchain can vectorize specific sections of regulation and make it possible to elicit relevant context through a simple App UI and let users pose questions, get accurate answers with correct citations, and even get actual drafts when further actions are required.

One of our team members has worked on streamlining and simplifying small business regulation for years (see, eg  Kansas  Kansas Business Center: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2485711 and conceptual prototype: https://www.youtube.com/live/DIyWeH-CGfM?feature=share). This proof of concept has demonstrated that small businesses can now engage with complex legal and regulatory requirements with an ease not before possible, and that is a high impact use of AI for Good!


# how to run locally:

```
uvicorn backend.api:app --host 0.0.0.0 --port 8124
```

Make sure to set you openai key in the env


To get a response from the model call `/generate` with this example payload:
```json{
    "query": "how many restrooms do I need",
    "user_profile": {
        "state": "CA",
        "business_type": "laundry",
        "num_employees": 150
    },
    "topic": "Sanitation"
}
```

for topic teh following options are allowed:
- Emergency Action Plan
- Laundry Machines
- Sanitation
