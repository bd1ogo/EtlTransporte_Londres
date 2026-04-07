-- Ver estrutura dos dados
SELECT * FROM transportes LIMIT 10;

-- Ver período total coberto
SELECT 
    MIN(period_beginning) AS inicio,
    MAX(period_ending) AS fim
FROM transportes;

-- Crescimento ao longo do tempo
SELECT 
    period_beginning,
    total_journeys
FROM transportes
ORDER BY period_beginning;

-- Comparação entre transporte público
SELECT 
    period_beginning,
    bus_journeys_m,
    underground_journeys_m
FROM transportes;

-- Identificar possíveis quedas (anomalias)
SELECT 
    period_beginning,
    total_journeys
FROM transportes
WHERE total_journeys < 200
ORDER BY total_journeys;

-- Participação percentual (modal)
SELECT
    SUM(bus_journeys_m) / SUM(total_journeys) * 100 AS perc_bus,
    SUM(underground_journeys_m) / SUM(total_journeys) * 100 AS perc_metro
FROM transportes;