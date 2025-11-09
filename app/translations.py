# translations.py - Bilingual support for English and Marathi

TRANSLATIONS = {
    'en': {
        # Navigation
        'home': 'Home',
        'buses': 'Buses',
        'routes': 'Routes',
        'schedules': 'Schedules',
        'crew': 'Crew',
        'dashboard': 'Dashboard',
        'reports': 'Reports',

        # Dashboard dropdown
        'analytics': 'Analytics',
        'live_tracking': 'Live Tracking (Operator)',
        'track_bus': 'Track Your Bus (User)',
        'live_demo': 'Live Demo',

        # Home page
        'welcome_title': 'Welcome to Bus Depot Management System',
        'welcome_subtitle': 'Efficient Fleet Management & Real-Time Tracking',
        'get_started': 'Get Started',
        'view_live_demo': 'View Live Demo',
        'about_system': 'About the System',
        'about_text': 'Our comprehensive bus management system provides real-time tracking, route optimization, crew management, and detailed analytics. Monitor your entire fleet from a single dashboard.',
        'key_features': 'Key Features',
        'feature_tracking': 'Real-Time GPS Tracking',
        'feature_tracking_desc': 'Track all buses live on interactive maps',
        'feature_management': 'Fleet Management',
        'feature_management_desc': 'Manage buses, routes, and schedules efficiently',
        'feature_analytics': 'Analytics Dashboard',
        'feature_analytics_desc': 'Comprehensive reports and visualizations',
        'feature_crew': 'Crew Management',
        'feature_crew_desc': 'Assign and track crew members',

        # Dashboard pages
        'operator_dashboard_title': 'Live Operator Dashboard',
        'active_buses': 'Active Buses',
        'total_fleet': 'Total Fleet',
        'connection_status': 'Socket.IO Status',
        'live_fleet_map': 'Live Fleet Map',
        'connecting': 'Connecting...',
        'connected': 'Connected',
        'disconnected': 'Disconnected',
        'offline_mode': 'Offline Mode',

        # User dashboard
        'track_your_bus': 'Track Your Bus',
        'select_route': 'Select Route',
        'choose_route': 'Choose a route...',
        'track_bus_btn': 'Track Bus',
        'bus_location': 'Bus Location',
        'speed': 'Speed',

        # Live demo
        'live_demo_title': 'Live Demo - Real-Time Tracking',

        # Common
        'loading': 'Loading...',
        'error': 'Error',
        'success': 'Success',
        'no_data': 'No data available',
    },

    'mr': {
        # Navigation (Marathi)
        'home': 'मुख्यपृष्ठ',
        'buses': 'बसेस',
        'routes': 'मार्ग',
        'schedules': 'वेळापत्रक',
        'crew': 'कर्मचारी',
        'dashboard': 'डॅशबोर्ड',
        'reports': 'अहवाल',

        # Dashboard dropdown
        'analytics': 'विश्लेषण',
        'live_tracking': 'लाइव्ह ट्रॅकिंग (ऑपरेटर)',
        'track_bus': 'तुमची बस शोधा',
        'live_demo': 'लाइव्ह डेमो',

        # Home page
        'welcome_title': 'बस डेपो व्यवस्थापन प्रणालीमध्ये आपले स्वागत आहे',
        'welcome_subtitle': 'कार्यक्षम फ्लीट व्यवस्थापन आणि रिअल-टाइम ट्रॅकिंग',
        'get_started': 'सुरुवात करा',
        'view_live_demo': 'लाइव्ह डेमो पहा',
        'about_system': 'प्रणालीबद्दल',
        'about_text': 'आमची सर्वसमावेशक बस व्यवस्थापन प्रणाली रिअल-टाइम ट्रॅकिंग, मार्ग ऑप्टिमायझेशन, क्रू व्यवस्थापन आणि तपशीलवार विश्लेषण प्रदान करते. एका डॅशबोर्डवरून तुमचा संपूर्ण ताफा मॉनिटर करा.',
        'key_features': 'मुख्य वैशिष्ट्ये',
        'feature_tracking': 'रिअल-टाइम GPS ट्रॅकिंग',
        'feature_tracking_desc': 'इंटरॅक्टिव्ह नकाशांवर सर्व बस लाइव्ह ट्रॅक करा',
        'feature_management': 'फ्लीट व्यवस्थापन',
        'feature_management_desc': 'बसेस, मार्ग आणि वेळापत्रक कार्यक्षमतेने व्यवस्थापित करा',
        'feature_analytics': 'विश्लेषण डॅशबोर्ड',
        'feature_analytics_desc': 'सर्वसमावेशक अहवाल आणि व्हिज्युअलायझेशन',
        'feature_crew': 'कर्मचारी व्यवस्थापन',
        'feature_crew_desc': 'कर्मचारी सदस्य नियुक्त करा आणि ट्रॅक करा',

        # Dashboard pages
        'operator_dashboard_title': 'लाइव्ह ऑपरेटर डॅशबोर्ड',
        'active_buses': 'सक्रिय बसेस',
        'total_fleet': 'एकूण ताफा',
        'connection_status': 'कनेक्शन स्थिती',
        'live_fleet_map': 'लाइव्ह फ्लीट नकाशा',
        'connecting': 'कनेक्ट होत आहे...',
        'connected': 'कनेक्ट केले',
        'disconnected': 'डिस्कनेक्ट केले',
        'offline_mode': 'ऑफलाइन मोड',

        # User dashboard
        'track_your_bus': 'तुमची बस शोधा',
        'select_route': 'मार्ग निवडा',
        'choose_route': 'मार्ग निवडा...',
        'track_bus_btn': 'बस ट्रॅक करा',
        'bus_location': 'बस स्थान',
        'speed': 'वेग',

        # Live demo
        'live_demo_title': 'लाइव्ह डेमो - रिअल-टाइम ट्रॅकिंग',

        # Common
        'loading': 'लोड होत आहे...',
        'error': 'त्रुटी',
        'success': 'यशस्वी',
        'no_data': 'डेटा उपलब्ध नाही',
    }
}

def get_translation(key, lang='en'):
    """Get translation for a key in specified language"""
    return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(key, key)
