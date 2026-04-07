-- Total de viagens por período
SELECT 
    reporting_period,
    SUM(total_journeys) AS total_viagens
FROM transportes
GROUP BY reporting_period
ORDER BY reporting_period;

-- Média de viagens por período
SELECT 
    AVG(total_journeys) AS media_viagens
FROM transportes;

-- Total de viagens por tipo de transporte
SELECT
    SUM(bus_journeys_m) AS total_bus,
    SUM(underground_journeys_m) AS total_metro,
    SUM(dlr_journeys_m) AS total_dlr,
    SUM(tram_journeys_m) AS total_tram,
    SUM(overground_journeys_m) AS total_overground
FROM transportes;

-- Top 5 períodos com mais movimento
SELECT 
    period_beginning,
    total_journeys
FROM transportes
ORDER BY total_journeys DESC
LIMIT 5;