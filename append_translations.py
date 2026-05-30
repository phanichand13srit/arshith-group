import re

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

en_add = """
        "ec-prod-title": "Featured <span class='highlight'>Organics</span>",
        "ec-prod-1": "Pure Wild Honey",
        "ec-prod-2": "Fresh Hass Avocados",
        "ec-prod-3": "Cold-Pressed Olive Oil",
        "ec-buy": "Add to Cart",
        "ec-rev-title": "Happy <span class='highlight'>Customers</span>",
        "ec-rev-1": "\\"The organic produce from Arshith Fresh is simply unmatched. The delivery is always on time, and the quality is superb!\\"",
        "ec-rev-2": "\\"I love the fact that everything is locally sourced. The wild honey is the best I've ever tasted.\\"",
        "ec-rev-buyer": "Verified Buyer",

        "it-proj-title": "Recent <span class='highlight'>Projects</span>",
        "it-proj-1": "Enterprise CRM Dashboard",
        "it-proj-desc-1": "A fully scalable, cloud-based CRM solution developed for a top-tier financial institution.",
        "it-proj-2": "AI Chatbot Integration",
        "it-proj-desc-2": "Implemented a machine learning-driven customer support bot, reducing ticket response times by 80%.",
        "it-rev-title": "Client <span class='highlight'>Testimonials</span>",
        "it-rev-1": "\\"Arshith Infotech delivered our backend systems flawlessly. Their technical expertise and dedication are truly world-class.\\"",
        "it-rev-role": "CTO, TechWave Corp",
        "it-rev-2": "\\"The digital marketing strategies they implemented doubled our inbound leads in just three months.\\"",
        "it-rev-role2": "Marketing Director",

        "bc-proj-title": "Success <span class='highlight'>Stories</span>",
        "bc-proj-1": "Global Market Expansion",
        "bc-proj-desc-1": "Guided a regional manufacturing firm into European markets, resulting in a 40% revenue increase.",
        "bc-proj-2": "Merger & Acquisition Strategy",
        "bc-proj-desc-2": "Facilitated a $50M acquisition, ensuring cultural alignment and operational synergy.",
        "bc-rev-title": "Executive <span class='highlight'>Testimonials</span>",
        "bc-rev-1": "\\"Suntech Solutions provided the strategic clarity we desperately needed. Their advisory transformed our operational efficiency.\\"",
        "bc-rev-role": "CEO, Global Logistics",
        "bc-rev-2": "\\"An incredible partnership. Their insights into financial risk management saved us millions during the market downturn.\\"",
        "bc-rev-role2": "CFO, Apex Holdings"
"""

te_add = """
        "ec-prod-title": "ప్రత్యేక <span class='highlight'>సేంద్రీయ ఉత్పత్తులు</span>",
        "ec-prod-1": "స్వచ్ఛమైన అడవి తేనె",
        "ec-prod-2": "తాజా అవకాడోలు",
        "ec-prod-3": "కోల్డ్-ప్రెస్డ్ ఆలివ్ ఆయిల్",
        "ec-buy": "కార్ట్‌కు జోడించు",
        "ec-rev-title": "సంతోషకరమైన <span class='highlight'>కస్టమర్లు</span>",
        "ec-rev-1": "\\"అర్షిత్ ఫ్రెష్ నుండి సేంద్రీయ ఉత్పత్తులు అద్భుతం. డెలివరీ ఎల్లప్పుడూ సమయానికి జరుగుతుంది, మరియు నాణ్యత చాలా బాగుంది!\\"",
        "ec-rev-2": "\\"ప్రతిదీ స్థానికంగా సేకరించబడటం నాకు ఇష్టం. అడవి తేనె నేను రుచి చూసిన వాటిలో ఉత్తమమైనది.\\"",
        "ec-rev-buyer": "ధృవీకరించబడిన కొనుగోలుదారు",

        "it-proj-title": "ఇటీవలి <span class='highlight'>ప్రాజెక్టులు</span>",
        "it-proj-1": "ఎంటర్‌ప్రైజ్ CRM డాష్‌బోర్డ్",
        "it-proj-desc-1": "అగ్రశ్రేణి ఆర్థిక సంస్థ కోసం అభివృద్ధి చేయబడిన పూర్తిగా స్కేలబుల్, క్లౌడ్-ఆధారిత CRM పరిష్కారం.",
        "it-proj-2": "AI చాట్‌బాట్ ఏకీకరణ",
        "it-proj-desc-2": "మెషిన్ లెర్నింగ్-ఆధారిత కస్టమర్ సపోర్ట్ బాట్‌ను అమలు చేసాము, టికెట్ ప్రతిస్పందన సమయాలను 80% తగ్గించాము.",
        "it-rev-title": "క్లయింట్ <span class='highlight'>టెస్టిమోనియల్స్</span>",
        "it-rev-1": "\\"అర్షిత్ ఇన్ఫోటెక్ మా బ్యాకెండ్ సిస్టమ్‌లను దోషరహితంగా పంపిణీ చేసింది. వారి నైపుణ్యం నిజంగా ప్రపంచ స్థాయిది.\\"",
        "it-rev-role": "CTO, టెక్‌వేవ్ కార్ప్",
        "it-rev-2": "\\"వారు అమలు చేసిన డిజిటల్ మార్కెటింగ్ వ్యూహాలు కేవలం మూడు నెలల్లో మా ఇన్‌బౌండ్ లీడ్‌లను రెట్టింపు చేశాయి.\\"",
        "it-rev-role2": "మార్కెటింగ్ డైరెక్టర్",

        "bc-proj-title": "విజయ <span class='highlight'>గాథలు</span>",
        "bc-proj-1": "గ్లోబల్ మార్కెట్ విస్తరణ",
        "bc-proj-desc-1": "ప్రాంతీయ ఉత్పాదక సంస్థకు యూరోపియన్ మార్కెట్లలో మార్గనిర్దేశం చేసాము, ఫలితంగా 40% ఆదాయం పెరిగింది.",
        "bc-proj-2": "విలీనం & కొనుగోలు వ్యూహం",
        "bc-proj-desc-2": "$50M కొనుగోలును సులభతరం చేసాము, సాంస్కృతిక అనుసంధానం మరియు కార్యాచరణ సమన్వయాన్ని నిర్ధారించాము.",
        "bc-rev-title": "ఎగ్జిక్యూటివ్ <span class='highlight'>టెస్టిమోనియల్స్</span>",
        "bc-rev-1": "\\"సన్‌టెక్ సొల్యూషన్స్ మాకు చాలా అవసరమైన వ్యూహాత్మక స్పష్టతను అందించింది. వారి సలహా మా కార్యాచరణ సామర్థ్యాన్ని మార్చింది.\\"",
        "bc-rev-role": "CEO, గ్లోబల్ లాజిస్టిక్స్",
        "bc-rev-2": "\\"నమ్మశక్యం కాని భాగస్వామ్యం. మార్కెట్ పతనం సమయంలో ఆర్థిక ప్రమాద నిర్వహణపై వారి అంతర్దృష్టులు మాకు మిలియన్లను ఆదా చేశాయి.\\"",
        "bc-rev-role2": "CFO, అపెక్స్ హోల్డింగ్స్"
"""

hi_add = """
        "ec-prod-title": "विशेष <span class='highlight'>जैविक उत्पाद</span>",
        "ec-prod-1": "शुद्ध जंगली शहद",
        "ec-prod-2": "ताजा एवोकाडो",
        "ec-prod-3": "कोल्ड-प्रेस्ड जैतून का तेल",
        "ec-buy": "कार्ट में डालें",
        "ec-rev-title": "खुश <span class='highlight'>ग्राहक</span>",
        "ec-rev-1": "\\"अर्शित फ्रेश के जैविक उत्पाद बस बेजोड़ हैं। डिलीवरी हमेशा समय पर होती है, और गुणवत्ता शानदार है!\\"",
        "ec-rev-2": "\\"मुझे यह तथ्य पसंद है कि सब कुछ स्थानीय रूप से प्राप्त किया जाता है। जंगली शहद सबसे अच्छा है जिसका मैंने कभी स्वाद लिया है।\\"",
        "ec-rev-buyer": "सत्यापित खरीदार",

        "it-proj-title": "हाल की <span class='highlight'>परियोजनाएं</span>",
        "it-proj-1": "एंटरप्राइज सीआरएम डैशबोर्ड",
        "it-proj-desc-1": "एक शीर्ष-स्तरीय वित्तीय संस्थान के लिए विकसित एक पूरी तरह से स्केलेबल, क्लाउड-आधारित सीआरएम समाधान।",
        "it-proj-2": "एआई चैटबॉट एकीकरण",
        "it-proj-desc-2": "मशीन लर्निंग-संचालित ग्राहक सहायता बॉट लागू किया, जिससे टिकट प्रतिक्रिया समय में 80% की कमी आई।",
        "it-rev-title": "क्लाइंट <span class='highlight'>प्रशंसापत्र</span>",
        "it-rev-1": "\\"अर्शित इन्फोटेक ने हमारे बैकएंड सिस्टम को त्रुटिहीन रूप से वितरित किया। उनकी तकनीकी विशेषज्ञता वास्तव में विश्व स्तरीय है।\\"",
        "it-rev-role": "सीटीओ, टेकवेव कॉर्प",
        "it-rev-2": "\\"उनके द्वारा लागू की गई डिजिटल मार्केटिंग रणनीतियों ने केवल तीन महीनों में हमारे इनबाउंड लीड को दोगुना कर दिया।\\"",
        "it-rev-role2": "विपणन निदेशक",

        "bc-proj-title": "सफलता की <span class='highlight'>कहानियां</span>",
        "bc-proj-1": "वैश्विक बाजार विस्तार",
        "bc-proj-desc-1": "यूरोपीय बाजारों में एक क्षेत्रीय निर्माण फर्म का मार्गदर्शन किया, जिसके परिणामस्वरूप 40% राजस्व वृद्धि हुई।",
        "bc-proj-2": "विलय और अधिग्रहण रणनीति",
        "bc-proj-desc-2": "$50M के अधिग्रहण को सुगम बनाया, सांस्कृतिक संरेखण और परिचालन तालमेल सुनिश्चित किया।",
        "bc-rev-title": "कार्यकारी <span class='highlight'>प्रशंसापत्र</span>",
        "bc-rev-1": "\\"सनटेक सॉल्यूशंस ने हमें रणनीतिक स्पष्टता प्रदान की जिसकी हमें सख्त जरूरत थी। उनकी सलाह ने हमारी परिचालन दक्षता को बदल दिया।\\"",
        "bc-rev-role": "सीईओ, ग्लोबल लॉजिस्टिक्स",
        "bc-rev-2": "\\"एक अविश्वसनीय साझेदारी। वित्तीय जोखिम प्रबंधन में उनकी अंतर्दृष्टि ने बाजार की मंदी के दौरान हमारे लाखों रुपये बचाए।\\"",
        "bc-rev-role2": "सीएफओ, एपेक्स होल्डिंग्स"
"""

kn_add = """
        "ec-prod-title": "ವೈಶಿಷ್ಟ್ಯಪೂರ್ಣ <span class='highlight'>ಸಾವಯವ ಉತ್ಪನ್ನಗಳು</span>",
        "ec-prod-1": "ಶುದ್ಧ ಕಾಡು ಜೇನುತುಪ್ಪ",
        "ec-prod-2": "ತಾಜಾ ಆವಕಾಡೊಗಳು",
        "ec-prod-3": "ಕೋಲ್ಡ್-ಪ್ರೆಸ್ಡ್ ಆಲಿವ್ ಎಣ್ಣೆ",
        "ec-buy": "ಕಾರ್ಟ್‌ಗೆ ಸೇರಿಸಿ",
        "ec-rev-title": "ಸಂತೋಷದ <span class='highlight'>ಗ್ರಾಹಕರು</span>",
        "ec-rev-1": "\\"ಅರ್ಶಿತ್ ಫ್ರೆಶ್‌ನ ಸಾವಯವ ಉತ್ಪನ್ನಗಳು ಸರಳವಾಗಿ ಸಾಟಿಯಿಲ್ಲ. ವಿತರಣೆಯು ಯಾವಾಗಲೂ ಸಮಯಕ್ಕೆ ಸರಿಯಾಗಿರುತ್ತದೆ ಮತ್ತು ಗುಣಮಟ್ಟವು ಅದ್ಭುತವಾಗಿದೆ!\\"",
        "ec-rev-2": "\\"ಎಲ್ಲವನ್ನೂ ಸ್ಥಳೀಯವಾಗಿ ಪಡೆಯಲಾಗಿದೆ ಎಂಬ ಅಂಶವನ್ನು ನಾನು ಇಷ್ಟಪಡುತ್ತೇನೆ. ಕಾಡು ಜೇನುತುಪ್ಪವು ನಾನು ರುಚಿ ನೋಡಿದ ಅತ್ಯುತ್ತಮವಾಗಿದೆ.\\"",
        "ec-rev-buyer": "ಪರಿಶೀಲಿಸಿದ ಖರೀದಿದಾರ",

        "it-proj-title": "ಇತ್ತೀಚಿನ <span class='highlight'>ಯೋಜನೆಗಳು</span>",
        "it-proj-1": "ಎಂಟರ್‌ಪ್ರೈಸ್ CRM ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "it-proj-desc-1": "ಉನ್ನತ ಮಟ್ಟದ ಹಣಕಾಸು ಸಂಸ್ಥೆಗಾಗಿ ಅಭಿವೃದ್ಧಿಪಡಿಸಿದ ಸಂಪೂರ್ಣ ಸ್ಕೇಲೆಬಲ್, ಕ್ಲೌಡ್-ಆಧಾರಿತ CRM ಪರಿಹಾರ.",
        "it-proj-2": "AI ಚಾಟ್‌ಬಾಟ್ ಏಕೀಕರಣ",
        "it-proj-desc-2": "ಯಂತ್ರ ಕಲಿಕೆ-ಚಾಲಿತ ಗ್ರಾಹಕ ಬೆಂಬಲ ಬಾಟ್ ಅನ್ನು ಜಾರಿಗೆ ತರಲಾಯಿತು, ಟಿಕೆಟ್ ಪ್ರತಿಕ್ರಿಯೆ ಸಮಯವನ್ನು 80% ರಷ್ಟು ಕಡಿಮೆ ಮಾಡಿತು.",
        "it-rev-title": "ಕ್ಲೈಂಟ್ <span class='highlight'>ಪ್ರಶಂಸಾಪತ್ರಗಳು</span>",
        "it-rev-1": "\\"ಅರ್ಶಿತ್ ಇನ್ಫೋಟೆಕ್ ನಮ್ಮ ಬ್ಯಾಕೆಂಡ್ ವ್ಯವಸ್ಥೆಗಳನ್ನು ದೋಷರಹಿತವಾಗಿ ತಲುಪಿಸಿದೆ. ಅವರ ತಾಂತ್ರಿಕ ಪರಿಣತಿ ನಿಜಕ್ಕೂ ವಿಶ್ವದರ್ಜೆಯದ್ದಾಗಿದೆ.\\"",
        "it-rev-role": "CTO, ಟೆಕ್‌ವೇವ್ ಕಾರ್ಪ್",
        "it-rev-2": "\\"ಅವರು ಜಾರಿಗೆ ತಂದ ಡಿಜಿಟಲ್ ಮಾರ್ಕೆಟಿಂಗ್ ತಂತ್ರಗಳು ಕೇವಲ ಮೂರು ತಿಂಗಳಲ್ಲಿ ನಮ್ಮ ಇನ್‌ಬೌಂಡ್ ಲೀಡ್‌ಗಳನ್ನು ದ್ವಿಗುಣಗೊಳಿಸಿದವು.\\"",
        "it-rev-role2": "ಮಾರ್ಕೆಟಿಂಗ್ ನಿರ್ದೇಶಕ",

        "bc-proj-title": "ಯಶಸ್ಸಿನ <span class='highlight'>ಕಥೆಗಳು</span>",
        "bc-proj-1": "ಜಾಗತಿಕ ಮಾರುಕಟ್ಟೆ ವಿಸ್ತರಣೆ",
        "bc-proj-desc-1": "ಯುರೋಪಿಯನ್ ಮಾರುಕಟ್ಟೆಗಳಿಗೆ ಪ್ರಾದೇಶಿಕ ಉತ್ಪಾದನಾ ಸಂಸ್ಥೆಗೆ ಮಾರ್ಗದರ್ಶನ ನೀಡಿದರು, ಇದರ ಪರಿಣಾಮವಾಗಿ 40% ಆದಾಯ ಹೆಚ್ಚಾಗಿದೆ.",
        "bc-proj-2": "ವಿಲೀನ ಮತ್ತು ಸ್ವಾಧೀನ ತಂತ್ರ",
        "bc-proj-desc-2": "$50M ಸ್ವಾಧೀನವನ್ನು ಸುಗಮಗೊಳಿಸಿದೆ, ಸಾಂಸ್ಕೃತಿಕ ಜೋಡಣೆ ಮತ್ತು ಕಾರ್ಯಾಚರಣೆಯ ಸಿನರ್ಜಿಯನ್ನು ಖಾತ್ರಿಪಡಿಸಿದೆ.",
        "bc-rev-title": "ಕಾರ್ಯನಿರ್ವಾಹಕ <span class='highlight'>ಪ್ರಶಂಸಾಪತ್ರಗಳು</span>",
        "bc-rev-1": "\\"ಸನ್‌ಟೆಕ್ ಸೊಲ್ಯೂಷನ್ಸ್ ನಮಗೆ ತೀವ್ರವಾಗಿ ಅಗತ್ಯವಿದ್ದ ಕಾರ್ಯತಂತ್ರದ ಸ್ಪಷ್ಟತೆಯನ್ನು ಒದಗಿಸಿತು. ಅವರ ಸಲಹೆಯು ನಮ್ಮ ಕಾರ್ಯಾಚರಣೆಯ ದಕ್ಷತೆಯನ್ನು ಪರಿವರ್ತಿಸಿತು.\\"",
        "bc-rev-role": "CEO, ಗ್ಲೋಬಲ್ ಲಾಜಿಸ್ಟಿಕ್ಸ್",
        "bc-rev-2": "\\"ನಂಬಲಾಗದ ಪಾಲುದಾರಿಕೆ. ಹಣಕಾಸಿನ ಅಪಾಯ ನಿರ್ವಹಣೆಯ ಕುರಿತಾದ ಅವರ ಒಳನೋಟಗಳು ಮಾರುಕಟ್ಟೆ ಕುಸಿತದ ಸಮಯದಲ್ಲಿ ನಮ್ಮ ಲಕ್ಷಾಂತರ ಹಣವನ್ನು ಉಳಿಸಿದವು.\\"",
        "bc-rev-role2": "CFO, ಅಪೆಕ್ಸ್ ಹೋಲ್ಡಿಂಗ್ಸ್"
"""

content = re.sub(r'("bc-lead-desc": "Partner with Suntech Solutions[^"]*"\s*)\}', r'\1,' + en_add + '    }', content)
content = re.sub(r'("bc-lead-desc": "అనుకూలీకరించిన కన్సల్టింగ్ సేవల ద్వారా[^"]*"\s*)\}', r'\1,' + te_add + '    }', content)
content = re.sub(r'("bc-lead-desc": "अनुकूलित परामर्श सेवाओं के माध्यम से[^"]*"\s*)\}', r'\1,' + hi_add + '    }', content)
content = re.sub(r'("bc-lead-desc": "ಸೂಕ್ತವಾದ ಸಲಹಾ ಸೇವೆಗಳ ಮೂಲಕ[^"]*"\s*)\}', r'\1,' + kn_add + '    }', content)

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Appended final translations.")
