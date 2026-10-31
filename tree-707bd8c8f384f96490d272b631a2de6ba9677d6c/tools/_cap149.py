"""Check candidate #149 caption strings against the text layer before recording."""

import sys
from pathlib import Path

LANE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LANE / "tools"))
import schema  # noqa: E402

PID = "P-B-2018-74316-1198d12d"

CAND = {
    (4, "t1"): "Table 1: Variables and Parameters for Model 1",
    (6, "t2"): "Table 2: List of Languages by Numbers of Speakers （Unit: Millions）",
    (6, "f1"): "Figure 1: Number of L1 Speakers",
    (6, "f2"): "Figure 2: Number of L2 Speakers",
    (6, "f3"): "Figure 3: Number of Total Speakers (Unit: Millions)",
    (6, "f4"): "Figure 4: Autocorrelation and Partial Correlation",
    (6, "f5"): "Figure 5: Autocorrelation and Partial Correlation",
    (7, "t3"): "Table 3: AR(1) Model for Different Languages",
    (7, "t4"): "Table 4: Akaike Information Criterion Test",
    (8, "t5"): "Table 5: EG Co-integration Test",
    (8, "t6"): "Table 6: Consequence of The First Step of EG Method",
    (10, "t7"): "Table 7: Consequence of The Second Step of EG Method",
    (10, "t8"): "Table 8: Consequence of Dickey-Fuller Test",
    (11, "f6"): "Figure 6: L1 Speakers Versus Time when N(0)>Nm",
    (11, "f7"): "Figure 7: L1 Speakers Versus Time when (δ=-0.1, Nm=1000)",
    (11, "f8"): "Figure 8: L1 Speakers Versus Time ( =0.1, Nm=1000)",
    (11, "f9"): "Figure 9: Total Speakers Versus Time for Different Initial Value ( =0.1, "
                "Nm=1000,  =3)",
    (12, "t9"): "Table 9: Approximation of Parameters in Long-term Models",
    (12, "f10"): "Figure 10: Number of Speakers Versus Time for Mandarin Chinese",
    (12, "t10"): "Table10: Predictions for current Top 10 Languages in Next 50 years",
    (13, "f11"): "Figure 11: Predictions for Malay and Russian",
    (13, "f12a"): "Figure 12: Number of Total Speakers for 4 Special Languages",
    (13, "t11"): "Table 11: Sensitivity Analysis on",
    (14, "t12"): "Table 12: Sensitivity Analysis on μ",
    (14, "f12b"): "Figure 12: Comprehensive Sensitivity Analysis for Mandarin Chinese",
    (14, "f13"): "Figure 13: Sensitivity Analysis on Initial Value of N for Russian Model",
    (15, "f14"): "Figure 14: Monte Carlo Simulation on L1 Speakers and Total Speakers for "
                 "Mandarin Chinese",
    (15, "t13"): "Table 13: Variables for Model 2",
    (17, "f15"): "Figure 15: Share of population born abroad of Each Country (Visualized "
                 "Moving-in Matrix M0 )",
    (17, "f16"): "Figure 16: Visualize G by The Mobile Average Data of Population Naturally "
                 "Growth Rate (2005-2016 Partially）",
    (18, "f17"): "Figure 17: Geographic Distribution of Mandarin Chinese in The Next 50 Years",
    (18, "t14"): "Table 14: Difference Between Predictions of 2 Models",
    (19, "f18"): "Figure 18: Cluster Dendrograms for 4 Vectors of Variables when t=5",
    (20, "t15"): "Table 15: Short-term results",
    (20, "t16"): "Table 16: Long-term results",
    (21, "f19"): "Figure 19: Distribution of MIC for Short-term Samples",
    (21, "f20"): "Figure 20: Geographic Distribution of 8",
    (21, "f21"): "Figure 21: Distribution of MIC after Improving",
    (22, "f22"): "Figure 22: Distribution of MIC for Original Plan",
    (22, "f23"): "Figure 23: Distribution of MIC for New Plan in Long-term",
    (24, "fx"): "Figure: Appropriate Locations of International Offices According to New Plan",
    (26, "a_hn"): "Autocorrelation and Partial Correlation of Hindustani",
    (26, "a_sp"): "Autocorrelation and Partial Correlation of Spanish",
    (26, "a_ml"): "Autocorrelation and Partial Correlation of Malay",
    (26, "a_ar"): "Autocorrelation and Partial Correlation of Arabic",
    (26, "a_ru"): "Autocorrelation and Partial Correlation of Russian",
    (26, "a_bn"): "Autocorrelation and Partial Correlation of Bengali",
    (26, "a_fr"): "Autocorrelation and Partial Correlation of FRE",
    (26, "a_pt"): "Autocorrelation and Partial Correlation of Portuguese",
    (28, "t2app"): "Table2: Formed Panel by factors influencing the number of non-native "
                   "speakers in2008-2016",
    (30, "f5app"): "Figure 5: Analysis Simulation for Prediction Error of Marinda Chinese "
                   "(Variance of Error Versus Prediction Step-length=1:50)",
    (37, "cap13"): "Appendix 13 3D Image of the Number of Particular Language Speakers – "
                   "Geographic Distribution",
    (27, "cap27"): "Appendix 2 Data for the Short-term Model of Non-native Speaker in Model 1",
    (29, "cap29a"): "Appendix 3 Threshold Tables for Cointegration Test of EG Method",
    (29, "cap29b"): "Appendix 4 Error Correction Terms of Each Language",
    (31, "cap31"): "Appendix 7 Number of Speakers Versus Time for Each Language",
    (32, "cap32"): "Appendix 8 Sensitivity Analysis Results of Each Language",
    (34, "cap34"): "Appendix 9 Part of Matrix Formed by the Number of Migrant in Different "
                   "Countries",
    (35, "cap35"): "Appendix 10 Part of One-Step Transition Probability Matrix",
    (36, "cap36"): "Appendix 11 Part of Population of countries in decades",
    (37, "cap37"): "Appendix 12 Part of Latitude and Longitude of Coordinates of Various "
                   "National Centers",
    (38, "cap38"): "Appendix 14 Variance Analysis Result",
    (39, "cap39a"): "Appendix 15 Score for Model 3 of Each Countries",
    (39, "cap39b"): "Appendix 16 National Comprehensive Evaluation Vector",
}

bad = 0
lines: list[str] = []
for (pg, key), text in CAND.items():
    if schema.norm(text) in schema.page_text(PID, pg):
        lines.append(f"ok   p{pg:>2} {key}")
    else:
        bad += 1
        lines.append(f"FAIL p{pg:>2} {key} :: {text[:90]!r}")
lines.append(f"failures={bad}/{len(CAND)}")
dest = LANE / ".proxy" / "_captions149.txt"
dest.write_text("\n".join(lines), encoding="utf-8")
print(f"failures={bad}/{len(CAND)}")
