/*Consulta para relacionar os usuários e plaquetas de patrimônio das máquinas aos centros de custo e estimar com maior precisão a ociosidade*/

SELECT *
,case when Marca = ' ' and DenominacaoImobilizado like '%Positivo%' then 'Positivo' Else Marca End Marca2
,case when Modelo = ' ' and DenominacaoImobilizado like '%Master D580%' then 'Master D580' Else Modelo End Modelo2
,DtIncorporacao, DATEDIFF(day, CONVERT(VARCHAR(50), CONVERT(DATE, DataCentroCusto), 23)  ,  CONVERT(VARCHAR(50), CONVERT(DATE, getdate()), 23)  ) DiasNoSetor
FROM
(
    SELECT DISTINCT 
           UG = aa.BUKRS, 
           Imobilizado = aa.ANLN1, 
           Plaqueta = aa.INVNR ,
                Plaqueta2 = SUBSTRING(aa.INVNR, PATINDEX('%[^0 ]%', aa.INVNR+' '), LEN(aa.INVNR)) COLLATE SQL_Latin1_General_CP1_CI_AS, -- REMOVE TODOS OS ZEROS A ESQUERDA
           --CodClasse = aa.ANLKL,
           CodClasse = SUBSTRING(aa.ANLKL, PATINDEX('%[^0 ]%', aa.ANLKL+' '), LEN(aa.ANLKL)), -- REMOVE TODOS OS ZEROS A ESQUERDA
           DescClasse = CLASSE.TXK50,

           DtIncorporacao2 = aa.AKTIV,
           CASE 
                           WHEN ISDATE(aa.AKTIV) = 0 THEN '01/01/9999'
                           ELSE  CONVERT(VARCHAR(50), CONVERT(DATE, aa.AKTIV), 103)
                    END AS DtIncorporacao,
                --DtIncorporacao = CONVERT(VARCHAR(50), CONVERT(DATE, aa.AKTIV), 103), 
           DenominacaoImobilizado = aa.TXT50, 
           DenominacaoComplementar = aa.TXA50,
           --,TxtPrincImobilizado = ah.ANLHTXT
           Marca = ORIGEM.YYMARCAMODELO, 
           Modelo = ORIGEM.YYMODELO, 
           Serie = aa.SERNR, 
               -- ORIGEM.YYGRUPO AS CodGrupo,
                GRUPO.DESCRICAO AS Grupo, 
                --ORIGEM.YYSUBGRUPO as Cod,
           SUBG.DESCR_SUB AS Subgrupo,

            CodCentroCusto = CASE 
                    WHEN CC.LTEXT like 'PJ%CACHO%' THEN '1010000101'
                    WHEN CC.LTEXT like 'PJ%LINHARES%' THEN '1010000102'
                    WHEN CC.LTEXT like 'PJ%COLATINA%' THEN '1010000100'
                    WHEN CC.LTEXT like 'PJ%CARIACI%' THEN '1010000093'  --PJ CARIACICA
                    WHEN CC.LTEXT like 'PJ%VIANA%' THEN '1010000097'
                    WHEN CC.LTEXT like 'PJ%SAO MATEUS%' OR CC.LTEXT like 'PJ%SÃO MATEUS%' THEN '1010000096'
                    WHEN CC.LTEXT like 'PJ%GUARAPARI%' THEN '1010000094'
                    WHEN CC.LTEXT like 'PJ%VILA VELHA%' THEN '1010000098'                                                      
             ELSE az.KOSTL
             END,     
             DescCentroCusto = CASE 
                    WHEN CC.LTEXT like 'PJ%CACHO%' THEN 'PJ DE CACHOEIRO DE ITAPEMIRIM'
                    WHEN CC.LTEXT like 'PJ%LINHARES%' THEN 'PJ DE LINHARES'
                    WHEN CC.LTEXT like 'PJ%COLATINA%' THEN 'PJ DE COLATINA'
                    WHEN CC.LTEXT like 'PJ%CARIACI%' THEN 'PJ CARIACICA' 
                    WHEN CC.LTEXT like 'PJ%VIANA%' THEN 'PJ DE VIANA'
                    WHEN CC.LTEXT like 'PJ%SAO MATEUS%' OR CC.LTEXT like 'PJ%SÃO MATEUS%' THEN 'PJ DE SAO MATEUS'
                    WHEN CC.LTEXT like 'PJ%GUARAPARI%' THEN 'PJ DE GUARAPARI'
                    WHEN CC.LTEXT like 'PJ%VILA VELHA%' THEN 'PJ DE VILA VELHA'
             ELSE CAST(CC.LTEXT AS varchar(60)) COLLATE sql_latin1_general_cp1251_ci_as -- REMOVER ACENTOS
             END,

           conservacao = CASE
                             WHEN ORIGEM.YYCOD_CLASS_BEM = 1
                             THEN 'Ótimo'
                             WHEN ORIGEM.YYCOD_CLASS_BEM = 2
                             THEN 'Bom'
                             WHEN ORIGEM.YYCOD_CLASS_BEM = 3
                             THEN 'Regular'
                             WHEN ORIGEM.YYCOD_CLASS_BEM = 4
                             THEN 'Inservivel'
                             WHEN ORIGEM.YYCOD_CLASS_BEM = 0
                             THEN 'desconhecido'
                         END, 

            DataCentroCusto = (SELECT MAX(az2.adatu) 
                    FROM [CLSQL02\SAPECP].ECP.ecp.ANLZ az2 
                    WHERE aa.ANLN1 = az2.ANLN1
                    AND aa.MANDT = az2.MANDT
            AND aa.ANLN2 = az2.ANLN2
            AND aa.BUKRS = az2.BUKRS),

           ORIGEM.YYVLR_AQUISICAO AS 'Origem - Valor da aquisição', 
           ORIGEM.YYDADOS_COMP AS 'Origem - Dados Complem.', 
           YYNUM_PROC_BAIXA AS 'Nº Processo Baixa', 
           YYDCR_PROCESSO AS 'Descrição do Processo Baixa', 
           YYFLG_BLOQ_BAIXA AS 'flag_bloqueio',
                CASE WHEN DEAKT = '00000000' THEN 'ATIVO' ELSE 'DESATIVADO EM ' +  CONVERT(VARCHAR(50), CONVERT(DATE, aa.DEAKT), 103)  END AS ATIVO

    FROM [CLSQL02\SAPECP].ECP.ecp.ANLA aa -- informações principais do dado mestre do imobilizado
         INNER JOIN [CLSQL02\SAPECP].ECP.ecp.ANLZ az ON aa.ANLN1 = az.ANLN1 -- informação de valor - para trazer o centro de custo
                                       AND aa.MANDT = az.MANDT
                                       AND aa.ANLN2 = az.ANLN2
                                       AND aa.BUKRS = az.BUKRS
         LEFT JOIN [CLSQL02\SAPECP].ECP.ecp.ANLH ah ON aa.ANLN1 = ah.ANLN1  -- para campo "Texto_Principal_Imob" do dado mestre
                                      AND aa.MANDT = ah.MANDT
                                      AND aa.BUKRS = ah.BUKRS
         JOIN [CLSQL02\SAPECP].ECP.ecp.ANKT CLASSE ON aa.MANDT = CLASSE.MANDT
                                     AND aa.ANLKL = CLASSE.ANLKL
                                     AND CLASSE.SPRAS = 'P' -- lingua Portugues
         LEFT JOIN [CLSQL02\SAPECP].ECP.ecp.ANLU ORIGEM ON aa.ANLN1 = ORIGEM.ANLN1
                                          AND aa.MANDT = ORIGEM.MANDT
                                          AND aa.ANLN2 = ORIGEM.ANLN2
                                          AND aa.BUKRS = ORIGEM.BUKRS

                  LEFT JOIN [CLSQL02\SAPECP].ECP.ecp.YTFIIMOB_GRUPOS GRUPO ON ORIGEM.YYGRUPO = GRUPO.GRUPO
                                                AND CLASSE.ANLKL = GRUPO.ANLKL
     LEFT JOIN
                    (
                           SELECT DISTINCT 
                                     *
                           FROM [CLSQL02\SAPECP].ECP.ecp.YVFI_CLGRPSU
                    ) SUBG ON ORIGEM.YYSUBGRUPO = SUBG.SUBGRUPO
                                    AND GRUPO.GRUPO = SUBG.GRUPO
                                    AND GRUPO.ANLKL = SUBG.ANLKL 
                            --AND CLASSE.ANLKL = SUBG.ANLKL

         LEFT JOIN
    (
        SELECT A.KOSTL, -- NÚMERO DO CC
               A.LTEXT -- NOME DO CC
        FROM [CLSQL02\SAPECP].ECP.ecp.CSKT A
             JOIN [CLSQL02\SAPECP].ECP.ecp.CSKS B ON A.KOSTL = B.KOSTL
                                                     AND B.KOKRS = 'MPES'
                                                     AND B.MANDT = 600
        WHERE A.MANDT = 600
              AND A.KOKRS LIKE 'MPES'
              AND B.DATBI > CONVERT(CHAR(8), GETDATE(), 112)
              AND A.DATBI > CONVERT(CHAR(8), GETDATE(), 112)
    ) CC ON az.KOSTL = CC.KOSTL
    WHERE aa.MANDT = 600
          AND (az.ADATU <= CONVERT(VARCHAR, GETDATE(), 112)
               AND az.BDATU >= CONVERT(VARCHAR, GETDATE(), 112))
      AND aa.DEAKT = '00000000'
) T


where T.CodClasse = '5235' --AND YYGRUPO = '15000000' --AND ( YYSUBGRUPO <> '15000004' AND YYSUBGRUPO <> '15000003') --( YYSUBGRUPO = '15000004' OR YYSUBGRUPO = '15000003')
             --AND DescCentroCusto LIKE 'GAECO - GRUPO COMBATE CRIME ORGANIZADO'
           --AND Subgrupo like 'Microcomputador (CPU)'
             AND DescCentroCusto <> 'SERVICO DE PATRIMONIO - INSERVIVEIS'
             AND DescCentroCusto <> 'CINF ATENDIMENTO'
             AND (Subgrupo like 'Notebook' OR Subgrupo like 'Microcomputador (CPU)')
             --AND DtIncorporacao2 < '20190601'