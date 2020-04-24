module.exports = app => {
    const covidMapData = require("../controllers/covid-map-data.controller.js");
    // Retrieve map data for last update
    app.get("/covid-map-data/last-updated", covidMapData.getLastUpdated);

    // Retrieve aggregate map data for last update
    app.get("/covid-map-data/aggregates", covidMapData.getAggregates);
  };