const graphql_language_service_server_1 = require("graphql-language-service-server");
process.on('uncaughtException', error => {
    process.stderr.write('An error was thrown from GraphQL language service: ' + String(error));
});
try {
    (0, graphql_language_service_server_1.startServer)({ method: 'stream' });
}
catch (error) {
    const logger = new graphql_language_service_server_1.Logger();
    logger.error(String(error));
}
process.stdin.on('close', () => {
    process.exit(0);
});
