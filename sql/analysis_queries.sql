-- 1. Fund House AUM
SELECT fund_house, SUM(aum_crore) AS total_aum_crore
FROM aum
GROUP BY fund_house
ORDER BY total_aum_crore DESC;


-- 2. Top 10 Schemes by 1-Year Return
SELECT
    f.amfi_code,
    f.scheme_name,
    p.return_1yr_pct
FROM fund_master f
JOIN performance p
ON f.amfi_code = p.amfi_code
ORDER BY p.return_1yr_pct DESC
LIMIT 10;


-- 3. Top 10 Schemes - Return vs Risk
SELECT
    f.scheme_name,
    p.return_1yr_pct,
    p.risk_grade,
    p.sharpe_ratio
FROM fund_master f
JOIN performance p
ON f.amfi_code = p.amfi_code
ORDER BY p.return_1yr_pct DESC
LIMIT 10;


-- 4. Top 10 Months by SIP Inflow
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM sip
ORDER BY sip_inflow_crore DESC
LIMIT 10;


-- 5. SIP Inflow Summary
SELECT
    ROUND(AVG(sip_inflow_crore), 2) AS average_sip_inflow,
    MAX(sip_inflow_crore) AS highest_sip_inflow,
    MIN(sip_inflow_crore) AS lowest_sip_inflow
FROM sip;


-- 6. Schemes by Risk Grade
SELECT
    risk_grade,
    COUNT(*) AS scheme_count
FROM performance
GROUP BY risk_grade
ORDER BY scheme_count DESC;


-- 7. Schemes by Fund House
SELECT
    fund_house,
    COUNT(*) AS scheme_count
FROM fund_master
GROUP BY fund_house
ORDER BY scheme_count DESC;