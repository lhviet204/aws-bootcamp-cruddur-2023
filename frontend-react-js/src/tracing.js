// tracing.js
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { WebTracerProvider, BatchSpanProcessor } from '@opentelemetry/sdk-trace-web';
import { ZoneContextManager } from '@opentelemetry/context-zone';
import { Resource }  from '@opentelemetry/resources';
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';

// import lib for propogate between FE and BE for xmlhttp and fetch
import { XMLHttpRequestInstrumentation } from '@opentelemetry/instrumentation-xml-http-request';
import { FetchInstrumentation } from '@opentelemetry/instrumentation-fetch';
import { registerInstrumentations } from '@opentelemetry/instrumentation';

const exporter = new OTLPTraceExporter({
  url: process.env.REACT_APP_OTLP_COLLECTOR_URL
});
const provider = new WebTracerProvider({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'cruddur-fe-react-js',
  }),
});
provider.addSpanProcessor(new BatchSpanProcessor(exporter));
provider.register({
  contextManager: new ZoneContextManager()
});

registerInstrumentations({
    instrumentations: [
      new XMLHttpRequestInstrumentation({
        propagateTraceHeaderCorsUrls: [
            new RegExp(`${process.env.REACT_APP_BACKEND_URL}`, 'g')
        ]
      }),
      new FetchInstrumentation({
        propagateTraceHeaderCorsUrls: [
            new RegExp(`${process.env.REACT_APP_BACKEND_URL}`, 'g')
        ]
      }),
      getWebAutoInstrumentations({
        // load custom configuration for xml-http-request instrumentation
        '@opentelemetry/instrumentation-xml-http-request': {
          propagateTraceHeaderCorsUrls: [
            new RegExp(`${process.env.REACT_APP_BACKEND_URL}`, 'g')
            ],
        },
        '@opentelemetry/instrumentation-fetch': {
          propagateTraceHeaderCorsUrls: [
            new RegExp(`${process.env.REACT_APP_BACKEND_URL}`, 'g')
            ],
        },
      }),
    ],
  });
  