# Week 2 — Distributed Tracing
- [Summary](#summary)
- [Homework](#homework)
- [Homework Challenges](#homework-challenges)

## Summary
## Homework
## Homework Challenges
There are two ways to implement monitor for traces between FE and BE
- Establish trace for FE, however there is not easy way to send trace driectly from enduser browsers to HONEYCOMB, you can technically do that with new only API key with "Send Event" permission only.

So, there is only way to implement so-called collector to collect traces from all end-user browsers before sending to HoneyComb.


## References
- https://docs.honeycomb.io/getting-data-in/opentelemetry/browser-js/#opentelemetry-in-the-browser

- https://docs.honeycomb.io/getting-data-in/otel-collector/

## Try Harder