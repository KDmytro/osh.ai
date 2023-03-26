# osh.ai


# how to run locally:

```
uvicorn backend.api:app --host 0.0.0.0 --port 8124
```

Make sure to set you openai key in the env


You cann call `/generate` with this example payload:
```json{
    "query": "how many restrooms do I need",
    "user_profile": {
        "state": "CA",
        "business_type": "laundry",
        "num_employees": 150
    },
    "topic": "Sanitation"
}

