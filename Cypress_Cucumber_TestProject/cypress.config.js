const { defineConfig } = require("cypress");
const {  addCucumberPreprocessorPlugin} = require("@badeball/cypress-cucumber-preprocessor");
const {  preprocessor} = require("@badeball/cypress-cucumber-preprocessor/browserify");
const sqlServer = require('cypress-sql-server');

async function setupNodeEvents(on, config) {
  
  config.db = {
    userName : "sa",
    password : "alpha123",
    server: "DESKTOP-0678FOK",
    options: {
        database: "NORTHWND",
        encrypt: true,
        rowCollectionOnRequestCompletion : true
    }
}
  tasks = sqlServer.loadDBPlugin(config.db);
  on('task', tasks);
  // This is required for the preprocessor to be able to generate JSON reports after each run, and more,
  await addCucumberPreprocessorPlugin(on, config);

  on("file:preprocessor", preprocessor(config));
  

  // Make sure to return the config object as it might have been modified by the plugin.
  return config;
}

module.exports = defineConfig({

  e2e: {
    setupNodeEvents,
    specPattern: "cypress/Integration/BDD/*.feature"
  },
  env:{
    url:"https://rahulshettyacademy.com/"

  }
});
