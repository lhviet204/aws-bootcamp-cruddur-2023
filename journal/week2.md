# Week 2 — Distributed Tracing
- [Summary](#summary)
- [Homework](#homework)
Instrument Honeycomb with OTEL
Instrument AWS X-Ray
Configure custom logger to send to CloudWatch Logs
Integrate Rollbar and capture and error
- [Homework Challenges](#homework-challenges)
- [ ] Instrument Honeycomb for the frontend-application to observe network latency between frontend and backend [HARD]
- [ ] Add custom instrumentation to Honeycomb to add more attributes eg. UserId, Add a custom span
- [ ] Run custom queries in Honeycomb and save them later eg. Latency by UserID, Recent Traces


## Summary
## Homework
## Homework Challenges

### <strong> Instrument Honeycomb for the frontend-application to observe network latency between frontend and backend [HARD] </strong>

There are two ways to implement monitor for traces between FE and BE
- Establish trace for FE, however there is not easy way to send trace driectly from enduser browsers to HONEYCOMB, you can technically do that with new only API key with "Send Event" permission only.

So, there is only way to implement so-called collector to collect traces from all end-user browsers before sending to HoneyComb.

By doing that, two steps are required :
- Establish collector, there is example on how to use Docker Collector, since we learn about Docker compose we will apply docker compose.
- Set up instrument for FE application

#### Establish collector
Following from honeycomb docs, the Collector consists of three components: receivers, processors, and exporters, which are then used to construct telemetry pipelines. All the components will be declared in file named "otel-collector-config.yaml" which we will mount to the docker for Collector.


#### Set up instrumentation
- Prepare the library from OT, and ensure it's included in package.json
- Prepare the tracing.js plus auto-propogate between FE and BE
- Add import 'tracing.js' on the index.js
- Input the local env for docker compose, OTEL collector yaml, and tracing.js

## References
- https://docs.honeycomb.io/getting-data-in/opentelemetry/browser-js/#opentelemetry-in-the-browser

- https://docs.honeycomb.io/getting-data-in/otel-collector/

https://github.com/open-telemetry/opentelemetry-collector/blob/main/config/configtls/README.md

https://github.com/open-telemetry/opentelemetry-collector/blob/main/config/configtls/README.md

https://opentelemetry.io/docs/instrumentation/js/exporters/

https://docs.honeycomb.io/getting-data-in/otel-collector/#cors-errors

https://docs.honeycomb.io/getting-data-in/opentelemetry/browser-js/

## Try Harder