# LSP-graphql

GraphQL support for Sublime's LSP plugin.

Uses [graphql-language-service-server](https://github.com/graphql/graphiql/tree/main/packages/graphql-language-service-server) to provide diagnostics, autocomplete suggestions, definitions and other features for GraphQL files or blocks. See linked repository for more information.

* Install [LSP](https://packagecontrol.io/packages/LSP), [GraphQL Sublime Package](https://packagecontrol.io/packages/GraphQL) and `LSP-graphql` from Package Control.
* Restart Sublime.

### Project configuration

Server requires that your project includes a configuration file that defines the `schema` URL at least. Refer to [server configuration file](https://github.com/graphql/graphiql/tree/main/packages/graphql-language-service-server#graphql-configuration-file-graphqlrcyml) for more details.


### Configuration

Open configuration file using command palette with `Preferences: LSP-graphql Settings` command or opening it from the Sublime menu (`Preferences > Package Settings > LSP > Servers > LSP-graphql`).
