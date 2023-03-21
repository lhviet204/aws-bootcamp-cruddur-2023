FROM envoyproxy/envoy:v1.25-latest

COPY envoy.yml /etc/envoy/envoy.yml
RUN chmod go+r /etc/envoy/envoy.yml

CMD ["envoy", "-c", "/etc/envoy/envoy.yml", "--log-level", "debug"]