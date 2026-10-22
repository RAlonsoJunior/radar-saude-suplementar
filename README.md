Radar da Saúde Suplementar
Evolução e concentração dos beneficiários de planos de saúde no Brasil (2021–2026).

# O case

Analista de uma consultoria de inteligência de mercado em saúde suplementar.Operadoras, corretoras e investidores consultam o time para decidir onde e como crescer.

# Perguntas de negócio

1. Como evoluiu o total de beneficiários (mai/2021 a ago/2026)?
2. Qual a cobertura (%) por UF e município? Onde estão os espaços de mercado?
3. Quanto do mercado as 10 maiores operadoras dominam (CR4/CR10, HHI)?
4. Individual vs. coletivo: quem cresce?
5. A carteira está envelhecendo (mix de faixas etárias)?
6. Quantas operadoras ativas por modalidade e como isso se relaciona com a concentração?


# Fontes de dados (públicas e gratuitas — verificadas em 22/10/2026)

1. ANS - Informações Consolidadas de Beneficiários (PDA-024, competencias 202105-202608):https://dadosabertos.ans.gov.br/FTP/PDA/informacoes_consolidadas_de_beneficiarios-024/
2. ANS - Operadoras Ativas (cadop, atualizado em 18/10/2026):https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/
3. IBGE - Estimativas de População:https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html


# Stack
Python (pandas, DuckDB) | SQL Server 2022 | Power BI | Excel | Figma | Git/GitHub


# Roadmap

Passo	    Entrega	                                    Status

S0	        Setup do ambiente e repo	                em andamento
S1	        Dicionário de dados + profiling	            a fazer
S2	        Download incremental dos CSVs	            a fazer
S3	        Staging no SQL Server	                    a fazer
S4	        Modelagem dimensional (star schema)	        a fazer
S5	        Carga incremental + qualidade de dados	    a fazer
S6	        Análises SQL (CTEs, window functions)	    a fazer
S7	        Estatística aplicada (HHI, CAGR)	        a fazer
S8	        Wireframes no Figma	                        a fazer
S9	        Dashboard Power BI (DAX)	                a fazer
S10	        Módulo Excel (Power Query)	                a fazer
S11	        QA final + documentação	                    a fazer
S12	        Insights e retrospectiva	                a fazer