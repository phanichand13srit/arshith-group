import json
import re

with open('translations.js', 'r', encoding='utf-8') as f:
    content = f.read()

en_add = """
        "ec-nav-link": "E-Commerce",
        "ec-hero-title": "Empowering Your<br>Digital Storefront",
        "ec-hero-desc": "End-to-end scalable e-commerce solutions for businesses of all sizes.",
        "ec-services-title": "Powerful <span class='highlight'>Features</span>",
        "ec-srv-mv": "Multi-Vendor Marketplaces",
        "ec-srv-mv-desc": "Build robust platforms that support multiple sellers, diverse inventory, and seamless payouts.",
        "ec-srv-pg": "Secure Payment Gateways",
        "ec-srv-pg-desc": "Integrate safe, reliable, and swift payment processing compatible with global financial networks.",
        "ec-srv-im": "Inventory Management",
        "ec-srv-im-desc": "Automate your stock tracking, alerts, and supply chain logistics in real-time.",
        "ec-srv-seo": "SEO & Analytics",
        "ec-srv-seo-desc": "Data-driven insights to maximize traffic, boost conversion rates, and understand customer behavior.",
        "ec-lead-title": "Start Selling Online",
        "ec-lead-desc": "Join hundreds of businesses leveraging Arshith Fresh's e-commerce ecosystem to reach millions of customers globally.",
        "bc-nav-link": "Business Consulting & Services",
        "bc-hero-title": "Strategic Guidance For<br>Unmatched Growth",
        "bc-hero-desc": "Expert consulting services designed to optimize operations, navigate challenges, and accelerate success.",
        "bc-services-title": "Our <span class='highlight'>Expertise</span>",
        "bc-srv-st": "Strategic Planning",
        "bc-srv-st-desc": "Develop long-term blueprints that align with your corporate vision, adapt to market shifts, and maximize ROI.",
        "bc-srv-hr": "Human Resources",
        "bc-srv-hr-desc": "Optimize workforce management, talent acquisition, and corporate culture to drive employee satisfaction.",
        "bc-srv-op": "Operations Management",
        "bc-srv-op-desc": "Streamline processes, reduce overhead costs, and implement efficient workflow methodologies.",
        "bc-srv-fa": "Financial Advisory",
        "bc-srv-fa-desc": "Gain insights through risk assessment, investment strategies, and corporate restructuring.",
        "bc-lead-title": "Transform Your Business",
        "bc-lead-desc": "Partner with Suntech Solutions to unlock your organization's true potential through tailored consulting services."
"""

te_add = """
        "ec-nav-link": "ఇ-కామర్స్",
        "ec-hero-title": "మీ డిజిటల్ స్టోర్‌ఫ్రంట్‌ను<br>సశక్తం చేయడం",
        "ec-hero-desc": "అన్ని పరిమాణాల వ్యాపారాల కోసం ఎండ్-టు-ఎండ్ స్కేలబుల్ ఇ-కామర్స్ పరిష్కారాలు.",
        "ec-services-title": "శక్తివంతమైన <span class='highlight'>లక్షణాలు</span>",
        "ec-srv-mv": "మల్టీ-వెండర్ మార్కెట్‌ప్లేస్‌లు",
        "ec-srv-mv-desc": "బహుళ విక్రేతలు, విభిన్న జాబితా మరియు అతుకులు లేని చెల్లింపులకు మద్దతు ఇచ్చే బలమైన ప్లాట్‌ఫారమ్‌లను రూపొందించండి.",
        "ec-srv-pg": "సురక్షిత చెల్లింపు గేట్‌వేలు",
        "ec-srv-pg-desc": "ప్రపంచ ఆర్థిక నెట్‌వర్క్‌లకు అనుకూలమైన సురక్షితమైన, విశ్వసనీయమైన మరియు వేగవంతమైన చెల్లింపు ప్రాసెసింగ్‌ను ఏకీకృతం చేయండి.",
        "ec-srv-im": "ఇన్వెంటరీ మేనేజ్‌మెంట్",
        "ec-srv-im-desc": "రియల్-టైమ్‌లో మీ స్టాక్ ట్రాకింగ్, హెచ్చరికలు మరియు సప్లై చైన్ లాజిస్టిక్స్‌ను ఆటోమేట్ చేయండి.",
        "ec-srv-seo": "SEO & విశ్లేషణలు",
        "ec-srv-seo-desc": "ట్రాఫిక్‌ను పెంచడానికి, మార్పిడి రేట్లను పెంచడానికి మరియు కస్టమర్ ప్రవర్తనను అర్థం చేసుకోవడానికి డేటా-ఆధారిత అంతర్దృష్టులు.",
        "ec-lead-title": "ఆన్‌లైన్‌లో విక్రయించడం ప్రారంభించండి",
        "ec-lead-desc": "ప్రపంచవ్యాప్తంగా మిలియన్ల మంది కస్టమర్లను చేరుకోవడానికి అర్షిత్ ఫ్రెష్ యొక్క ఇ-కామర్స్ పర్యావరణ వ్యవస్థను ప్రభావితం చేసే వందలాది వ్యాపారాలలో చేరండి.",
        "bc-nav-link": "వ్యాపార కన్సల్టింగ్ & సేవలు",
        "bc-hero-title": "సాటిలేని వృద్ధికి<br>వ్యూహాత్మక మార్గదర్శకత్వం",
        "bc-hero-desc": "కార్యకలాపాలను ఆప్టిమైజ్ చేయడానికి, సవాళ్లను నావిగేట్ చేయడానికి మరియు విజయాన్ని వేగవంతం చేయడానికి రూపొందించిన నిపుణుల కన్సల్టింగ్ సేవలు.",
        "bc-services-title": "మా <span class='highlight'>నైపుణ్యం</span>",
        "bc-srv-st": "వ్యూహాత్మక ప్రణాళిక",
        "bc-srv-st-desc": "మీ కార్పొరేట్ దృష్టితో సమలేఖనం చేసే, మార్కెట్ మార్పులకు అనుగుణంగా మరియు ROIని పెంచే దీర్ఘకాలిక బ్లూప్రింట్‌లను అభివృద్ధి చేయండి.",
        "bc-srv-hr": "మానవ వనరులు",
        "bc-srv-hr-desc": "ఉద్యోగుల సంతృప్తిని పెంచడానికి వర్క్‌ఫోర్స్ మేనేజ్‌మెంట్, టాలెంట్ అక్విజిషన్ మరియు కార్పొరేట్ సంస్కృతిని ఆప్టిమైజ్ చేయండి.",
        "bc-srv-op": "ఆపరేషన్స్ మేనేజ్‌మెంట్",
        "bc-srv-op-desc": "ప్రక్రియలను క్రమబద్ధీకరించండి, ఓవర్‌హెడ్ ఖర్చులను తగ్గించండి మరియు సమర్థవంతమైన వర్క్‌ఫ్లో పద్ధతులను అమలు చేయండి.",
        "bc-srv-fa": "ఆర్థిక సలహా",
        "bc-srv-fa-desc": "ప్రమాద అంచనా, పెట్టుబడి వ్యూహాలు మరియు కార్పొరేట్ పునర్నిర్మాణం ద్వారా అంతర్దృష్టులను పొందండి.",
        "bc-lead-title": "మీ వ్యాపారాన్ని మార్చండి",
        "bc-lead-desc": "అనుకూలీకరించిన కన్సల్టింగ్ సేవల ద్వారా మీ సంస్థ యొక్క నిజమైన సామర్థ్యాన్ని అన్‌లాక్ చేయడానికి సన్‌టెక్ సొల్యూషన్స్‌తో భాగస్వామి కండి."
"""

hi_add = """
        "ec-nav-link": "ई-कॉमर्स",
        "ec-hero-title": "आपके डिजिटल स्टोरफ्रंट को<br>सशक्त बनाना",
        "ec-hero-desc": "सभी आकार के व्यवसायों के लिए एंड-टू-एंड स्केलेबल ई-कॉमर्स समाधान।",
        "ec-services-title": "शक्तिशाली <span class='highlight'>विशेषताएं</span>",
        "ec-srv-mv": "मल्टी-वेंडर मार्केटप्लेस",
        "ec-srv-mv-desc": "मजबूत प्लेटफ़ॉर्म बनाएं जो कई विक्रेताओं, विविध इन्वेंट्री और निर्बाध भुगतान का समर्थन करते हों।",
        "ec-srv-pg": "सुरक्षित भुगतान गेटवे",
        "ec-srv-pg-desc": "वैश्विक वित्तीय नेटवर्क के साथ संगत सुरक्षित, विश्वसनीय और तेज़ भुगतान प्रसंस्करण को एकीकृत करें।",
        "ec-srv-im": "इन्वेंटरी प्रबंधन",
        "ec-srv-im-desc": "वास्तविक समय में अपने स्टॉक ट्रैकिंग, अलर्ट और आपूर्ति श्रृंखला रसद को स्वचालित करें।",
        "ec-srv-seo": "एसईओ और एनालिटिक्स",
        "ec-srv-seo-desc": "यातायात को अधिकतम करने, रूपांतरण दरों को बढ़ावा देने और ग्राहक व्यवहार को समझने के लिए डेटा-संचालित अंतर्दृष्टि।",
        "ec-lead-title": "ऑनलाइन बेचना शुरू करें",
        "ec-lead-desc": "विश्व स्तर पर लाखों ग्राहकों तक पहुंचने के लिए अर्शित फ्रेश के ई-कॉमर्स इकोसिस्टम का लाभ उठाने वाले सैकड़ों व्यवसायों में शामिल हों।",
        "bc-nav-link": "व्यापार परामर्श और सेवाएं",
        "bc-hero-title": "अद्वितीय विकास के लिए<br>रणनीतिक मार्गदर्शन",
        "bc-hero-desc": "संचालन को अनुकूलित करने, चुनौतियों से निपटने और सफलता में तेजी लाने के लिए डिज़ाइन की गई विशेषज्ञ परामर्श सेवाएं।",
        "bc-services-title": "हमारी <span class='highlight'>विशेषज्ञता</span>",
        "bc-srv-st": "रणनीतिक योजना",
        "bc-srv-st-desc": "दीर्घकालिक ब्लूप्रिंट विकसित करें जो आपके कॉर्पोरेट दृष्टिकोण के साथ संरेखित हों, बाजार में बदलाव के अनुकूल हों और आरओआई को अधिकतम करें।",
        "bc-srv-hr": "मानव संसाधन",
        "bc-srv-hr-desc": "कर्मचारी संतुष्टि बढ़ाने के लिए कार्यबल प्रबंधन, प्रतिभा अधिग्रहण और कॉर्पोरेट संस्कृति को अनुकूलित करें।",
        "bc-srv-op": "संचालन प्रबंधन",
        "bc-srv-op-desc": "प्रक्रियाओं को सुव्यवस्थित करें, ओवरहेड लागत कम करें और कुशल वर्कफ़्लो पद्धतियों को लागू करें।",
        "bc-srv-fa": "वित्तीय सलाहकार",
        "bc-srv-fa-desc": "जोखिम मूल्यांकन, निवेश रणनीतियों और कॉर्पोरेट पुनर्गठन के माध्यम से अंतर्दृष्टि प्राप्त करें।",
        "bc-lead-title": "अपने व्यवसाय को बदलें",
        "bc-lead-desc": "अनुकूलित परामर्श सेवाओं के माध्यम से अपने संगठन की वास्तविक क्षमता को अनलॉक करने के लिए सनटेक सॉल्यूशंस के साथ भागीदार बनें।"
"""

kn_add = """
        "ec-nav-link": "ಇ-ಕಾಮರ್ಸ್",
        "ec-hero-title": "ನಿಮ್ಮ ಡಿಜಿಟಲ್ ಸ್ಟೋರ್‌ಫ್ರಂಟ್ ಅನ್ನು<br>ಸಬಲೀಕರಣಗೊಳಿಸುವುದು",
        "ec-hero-desc": "ಎಲ್ಲಾ ಗಾತ್ರದ ವ್ಯವಹಾರಗಳಿಗೆ ಎಂಡ್-ಟು-ಎಂಡ್ ಸ್ಕೇಲೆಬಲ್ ಇ-ಕಾಮರ್ಸ್ ಪರಿಹಾರಗಳು.",
        "ec-services-title": "ಶಕ್ತಿಯುತ <span class='highlight'>ವೈಶಿಷ್ಟ್ಯಗಳು</span>",
        "ec-srv-mv": "ಮಲ್ಟಿ-ವೆಂಡರ್ ಮಾರುಕಟ್ಟೆ ಸ್ಥಳಗಳು",
        "ec-srv-mv-desc": "ಬಹು ಮಾರಾಟಗಾರರು, ವೈವಿಧ್ಯಮಯ ದಾಸ್ತಾನು ಮತ್ತು ತಡೆರಹಿತ ಪಾವತಿಗಳನ್ನು ಬೆಂಬಲಿಸುವ ದೃಢವಾದ ವೇದಿಕೆಗಳನ್ನು ನಿರ್ಮಿಸಿ.",
        "ec-srv-pg": "ಸುರಕ್ಷಿತ ಪಾವತಿ ಗೇಟ್‌ವೇಗಳು",
        "ec-srv-pg-desc": "ಜಾಗತಿಕ ಹಣಕಾಸು ನೆಟ್‌ವರ್ಕ್‌ಗಳೊಂದಿಗೆ ಹೊಂದಿಕೊಳ್ಳುವ ಸುರಕ್ಷಿತ, ವಿಶ್ವಾಸಾರ್ಹ ಮತ್ತು ತ್ವರಿತ ಪಾವತಿ ಪ್ರಕ್ರಿಯೆಯನ್ನು ಸಂಯೋಜಿಸಿ.",
        "ec-srv-im": "ಇನ್ವೆಂಟರಿ ಮ್ಯಾನೇಜ್ಮೆಂಟ್",
        "ec-srv-im-desc": "ನೈಜ ಸಮಯದಲ್ಲಿ ನಿಮ್ಮ ಸ್ಟಾಕ್ ಟ್ರ್ಯಾಕಿಂಗ್, ಎಚ್ಚರಿಕೆಗಳು ಮತ್ತು ಪೂರೈಕೆ ಸರಪಳಿ ಲಾಜಿಸ್ಟಿಕ್ಸ್ ಅನ್ನು ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಿ.",
        "ec-srv-seo": "SEO ಮತ್ತು ವಿಶ್ಲೇಷಣೆಗಳು",
        "ec-srv-seo-desc": "ಟ್ರಾಫಿಕ್ ಅನ್ನು ಹೆಚ್ಚಿಸಲು, ಪರಿವರ್ತನೆ ದರಗಳನ್ನು ಹೆಚ್ಚಿಸಲು ಮತ್ತು ಗ್ರಾಹಕರ ನಡವಳಿಕೆಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಡೇಟಾ-ಚಾಲಿತ ಒಳನೋಟಗಳು.",
        "ec-lead-title": "ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಮಾರಾಟವನ್ನು ಪ್ರಾರಂಭಿಸಿ",
        "ec-lead-desc": "ಜಾಗತಿಕವಾಗಿ ಲಕ್ಷಾಂತರ ಗ್ರಾಹಕರನ್ನು ತಲುಪಲು ಅರ್ಶಿತ್ ಫ್ರೆಶ್‌ನ ಇ-ಕಾಮರ್ಸ್ ಪರಿಸರ ವ್ಯವಸ್ಥೆಯನ್ನು ಬಳಸಿಕೊಳ್ಳುವ ನೂರಾರು ವ್ಯವಹಾರಗಳಿಗೆ ಸೇರಿಕೊಳ್ಳಿ.",
        "bc-nav-link": "ವ್ಯಾಪಾರ ಸಲಹಾ ಮತ್ತು ಸೇವೆಗಳು",
        "bc-hero-title": "ಸಾಟಿಯಿಲ್ಲದ ಬೆಳವಣಿಗೆಗೆ<br>ಕಾರ್ಯತಂತ್ರದ ಮಾರ್ಗದರ್ಶನ",
        "bc-hero-desc": "ಕಾರ್ಯಾಚರಣೆಗಳನ್ನು ಉತ್ತಮಗೊಳಿಸಲು, ಸವಾಲುಗಳನ್ನು ನ್ಯಾವಿಗೇಟ್ ಮಾಡಲು ಮತ್ತು ಯಶಸ್ಸನ್ನು ವೇಗಗೊಳಿಸಲು ವಿನ್ಯಾಸಗೊಳಿಸಲಾದ ತಜ್ಞರ ಸಲಹಾ ಸೇವೆಗಳು.",
        "bc-services-title": "ನಮ್ಮ <span class='highlight'>ಪರಿಣತಿ</span>",
        "bc-srv-st": "ಕಾರ್ಯತಂತ್ರದ ಯೋಜನೆ",
        "bc-srv-st-desc": "ನಿಮ್ಮ ಕಾರ್ಪೊರೇಟ್ ದೃಷ್ಟಿಗೆ ಹೊಂದಿಕೊಳ್ಳುವ, ಮಾರುಕಟ್ಟೆ ಬದಲಾವಣೆಗಳಿಗೆ ಹೊಂದಿಕೊಳ್ಳುವ ಮತ್ತು ROI ಅನ್ನು ಗರಿಷ್ಠಗೊಳಿಸುವ ದೀರ್ಘಕಾಲೀನ ಬ್ಲೂಪ್ರಿಂಟ್‌ಗಳನ್ನು ಅಭಿವೃದ್ಧಿಪಡಿಸಿ.",
        "bc-srv-hr": "ಮಾನವ ಸಂಪನ್ಮೂಲ",
        "bc-srv-hr-desc": "ಉದ್ಯೋಗಿಗಳ ತೃಪ್ತಿಯನ್ನು ಹೆಚ್ಚಿಸಲು ಕಾರ್ಯಪಡೆ ನಿರ್ವಹಣೆ, ಪ್ರತಿಭೆ ಸ್ವಾಧೀನ ಮತ್ತು ಕಾರ್ಪೊರೇಟ್ ಸಂಸ್ಕೃತಿಯನ್ನು ಉತ್ತಮಗೊಳಿಸಿ.",
        "bc-srv-op": "ಕಾರ್ಯಾಚರಣೆಗಳ ನಿರ್ವಹಣೆ",
        "bc-srv-op-desc": "ಪ್ರಕ್ರಿಯೆಗಳನ್ನು ಸುಗಮಗೊಳಿಸಿ, ಓವರ್ಹೆಡ್ ವೆಚ್ಚಗಳನ್ನು ಕಡಿಮೆ ಮಾಡಿ ಮತ್ತು ಸಮರ್ಥ ಕೆಲಸದ ಹರಿವಿನ ವಿಧಾನಗಳನ್ನು ಜಾರಿಗೆ ತನ್ನಿ.",
        "bc-srv-fa": "ಹಣಕಾಸು ಸಲಹಾ",
        "bc-srv-fa-desc": "ಅಪಾಯದ ಮೌಲ್ಯಮಾಪನ, ಹೂಡಿಕೆ ತಂತ್ರಗಳು ಮತ್ತು ಕಾರ್ಪೊರೇಟ್ ಪುನರ್ರಚನೆಯ ಮೂಲಕ ಒಳನೋಟಗಳನ್ನು ಪಡೆಯಿರಿ.",
        "bc-lead-title": "ನಿಮ್ಮ ವ್ಯಾಪಾರವನ್ನು ಪರಿವರ್ತಿಸಿ",
        "bc-lead-desc": "ಸೂಕ್ತವಾದ ಸಲಹಾ ಸೇವೆಗಳ ಮೂಲಕ ನಿಮ್ಮ ಸಂಸ್ಥೆಯ ನೈಜ ಸಾಮರ್ಥ್ಯವನ್ನು ಅನ್‌ಲಾಕ್ ಮಾಡಲು ಸನ್‌ಟೆಕ್ ಸೊಲ್ಯೂಷನ್ಸ್‌ನೊಂದಿಗೆ ಪಾಲುದಾರರಾಗಿ."
"""

# For each section, append before the closing bracket of the dict
content = re.sub(r'("it-btn-partner": "Partner With Us"\s*)\}', r'\1,' + en_add + '    }', content)
content = re.sub(r'("it-btn-partner": "మాతో భాగస్వామి కండి"\s*)\}', r'\1,' + te_add + '    }', content)
content = re.sub(r'("it-btn-partner": "हमारे साथ भागीदार बनें"\s*)\}', r'\1,' + hi_add + '    }', content)
content = re.sub(r'("it-btn-partner": "ನಮ್ಮೊಂದಿಗೆ ಪಾಲುದಾರರಾಗಿ"\s*)\}', r'\1,' + kn_add + '    }', content)

with open('translations.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Translations updated.")
