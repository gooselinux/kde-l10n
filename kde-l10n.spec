%define buildall 0

Name: kde-l10n
Version: 4.3.4
Release: 5%{dist}
Url: http://www.kde.org
Summary: Internationalization support for KDE
Group: User Interface/Desktops
License: LGPLv2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-ar-%{version}.tar.bz2
Source2: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-bg-%{version}.tar.bz2
Source3: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-ca-%{version}.tar.bz2
Source4: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-cs-%{version}.tar.bz2
Source5: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-csb-%{version}.tar.bz2
Source6: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-da-%{version}.tar.bz2
Source7: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-de-%{version}.tar.bz2
Source8: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-el-%{version}.tar.bz2
Source9: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-en_GB-%{version}.tar.bz2
Source11: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-es-%{version}.tar.bz2
Source12: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-et-%{version}.tar.bz2
Source13: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-eu-%{version}.tar.bz2
Source14: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-fi-%{version}.tar.bz2
Source15: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-fr-%{version}.tar.bz2
Source16: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-ga-%{version}.tar.bz2
Source17: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-gl-%{version}.tar.bz2
Source18: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-hi-%{version}.tar.bz2
Source19: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-hu-%{version}.tar.bz2
Source20: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-it-%{version}.tar.bz2
Source21: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-ja-%{version}.tar.bz2
Source22: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-km-%{version}.tar.bz2
Source23: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-ko-%{version}.tar.bz2
Source24: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-ku-%{version}.tar.bz2
Source25: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-lv-%{version}.tar.bz2
Source26: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-lt-%{version}.tar.bz2
Source27: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-mk-%{version}.tar.bz2
Source28: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-ml-%{version}.tar.bz2
Source29: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-nb-%{version}.tar.bz2
Source30: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-nds-%{version}.tar.bz2
Source32: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-nl-%{version}.tar.bz2
Source33: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-nn-%{version}.tar.bz2
Source34: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-pa-%{version}.tar.bz2
Source35: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-pl-%{version}.tar.bz2
Source36: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-pt-%{version}.tar.bz2
Source37: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-pt_BR-%{version}.tar.bz2
Source38: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-ru-%{version}.tar.bz2
Source40: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-sk-%{version}.tar.bz2
Source41: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-sl-%{version}.tar.bz2
Source42: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-sv-%{version}.tar.bz2
Source44: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-th-%{version}.tar.bz2
Source45: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-tr-%{version}.tar.bz2
Source46: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-uk-%{version}.tar.bz2
Source47: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-wa-%{version}.tar.bz2
Source48: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-zh_CN-%{version}.tar.bz2
Source49: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-zh_TW-%{version}.tar.bz2
Source50: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-sr-%{version}.tar.bz2
Source51: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-fy-%{version}.tar.bz2
Source52: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-kk-%{version}.tar.bz2
Source53: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-he-%{version}.tar.bz2
Source54: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-bn_IN-%{version}.tar.bz2
Source55: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-gu-%{version}.tar.bz2
Source56: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-is-%{version}.tar.bz2
Source57: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-kn-%{version}.tar.bz2
Source58: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-mai-%{version}.tar.bz2
Source59: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-mr-%{version}.tar.bz2
Source60: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-ro-%{version}.tar.bz2
Source61: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-tg-%{version}.tar.bz2
Source62: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-hr-%{version}.tar.bz2
Source63: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kde-l10n/%{name}-hne-%{version}.tar.bz2
Source1000: subdirs-kde-l10n

BuildRequires: cmake
BuildRequires: findutils
BuildRequires: gettext
BuildRequires: kdelibs4-devel >= 4.3 

Requires: kde-filesystem

%description
Internationalization support for KDE

%package Afrikaans
Summary: Afrikaans language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-af = %{version}-%{release}

%description Afrikaans
Afrikaans support for KDE

%package Arabic 
Summary: Arabic language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ar = %{version}-%{release}

%description Arabic
Arabic support for KDE

%package Azerbaijani
Summary: Azerbaijani language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-af = %{version}-%{release}

%description Azerbaijani
Azerbaijani language support for KDE

%package Basque
Summary: Basque language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-eu = %{version}-%{release}

%description Basque
Basque language support for KDE

%package Belarusian
Summary: Belarusian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-be = %{version}-%{release}

%description Belarusian
Belarusian language support for KDE

%package Bengali-India
Summary: Bengali India language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-bn_IN = %{version}-%{release}

%description Bengali-India
Bengali India language support for KDE

%package Bulgarian
Summary: Bulgarian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-bg = %{version}-%{release}

%description Bulgarian
Bulgarian language support for KDE

%package Tibetan
Summary: Tibetan language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-bo = %{version}-%{release}

%description Tibetan
Tibetan language support for KDE

%package Breton
Summary: Breton language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-br = %{version}-%{release}

%description Breton
Breton language support for KDE

%package Bosnian
Summary: Bosnian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-bs = %{version}-%{release}

%description Bosnian
Bosnian language support for KDE

%package Catalan
Summary: Catalan language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ca = %{version}-%{release}

%description Catalan
Catalan language support for KDE

%package Czech
Summary: Czech language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-cs = %{version}-%{release}

%description Czech
Czech language support for KDE

%package Welsh
Summary: Welsh language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-cy = %{version}-%{release}

%description Welsh
Welsh language support for KDE

%package Danish
Summary: Danish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-da = %{version}-%{release}

%description Danish
Danish language support for KDE

%package German
Summary: German language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-de = %{version}-%{release}

%description German
German language support for KDE

%package Greek
Summary: Greek language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-el = %{version}-%{release}

%description Greek
Greek language support for KDE

%package Gujarati
Summary: Gujarati language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gu = %{version}-%{release}

%description Gujarati
Gujarati language support for KDE

%package British
Summary: British English support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-en_GB = %{version}-%{release}

%description British
British English language support for KDE

%package Esperanto
Summary: Esperanto support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-eo = %{version}-%{release}

%description Esperanto
Esperanto support for KDE

%package Spanish
Summary: Spanish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-es = %{version}-%{release}

%description Spanish
Spanish language support for KDE

%package Estonian
Summary: Estonian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-et = %{version}-%{release}

%description Estonian
Estonian language support for KDE

%package Farsi
Summary: Farsi language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-fa = %{version}-%{release}

%description Farsi
Farsi language support for KDE

%package Finnish
Summary: Finnish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-fi = %{version}-%{release}

%description Finnish
Finnish language support for KDE

%package Faroese
Summary: Faroese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-fo = %{version}-%{release}

%description Faroese
Faroese language support for KDE

%package French
Summary: French language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-fr = %{version}-%{release}

%description French
French language support for KDE

%package Frisian
Summary: Frisian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-fy = %{version}-%{release}

%description Frisian
Frisian language support for KDE

%package Irish
Summary: Irish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ga = %{version}-%{release}

%description Irish
Irish language support for KDE

%package Galician
Summary: Galician language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-gl = %{version}-%{release}

%description Galician
Galician language support for KDE

%package Hebrew
Summary: Hebrew language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-he = %{version}-%{release}

%description Hebrew
Hebrew language support for KDE

%package Hindi
Summary: Hindi language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-hi = %{version}-%{release}

%description Hindi
%{summary}.

%package Chhattisgarhi 
Summary: Chhattisgarhi language support for KDE 
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-hne = %{version}-%{release}

%description Chhattisgarhi 
%{summary}.

%package Croatian
Summary: Croatian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-hr = %{version}-%{release}

%description Croatian
Croatian language support for KDE

%package Hungarian
Summary: Hungarian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-hu = %{version}-%{release}

%description Hungarian
Hungarian language support for KDE

%package Indonesian
Summary: Indonesian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-id = %{version}-%{release}

%description Indonesian
Indonesian language support for KDE

%package Icelandic
Summary: Icelandic language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-is = %{version}-%{release}

%description Icelandic
Icelandic language support for KDE

%package Italian
Summary: Italian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-it = %{version}-%{release}

%description Italian
Italian language support for KDE

%package Japanese
Summary: Japanese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ja = %{version}-%{release}

%description Japanese
Japanese language support for KDE

%package Kannada
Summary: Kannada language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-kn = %{version}-%{release}

%description Kannada
Kannada language support for KDE

%package Kashubian
Summary: Kashubian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-csb = %{version}-%{release}

%description Kashubian
Kashubian language support for KDE

%package Kazakh
Summary: Kazakh language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-kk = %{version}-%{release}

%description Kazakh
Kazakh language support for KDE

%package Khmer
Summary: Khmer language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-km = %{version}-%{release}

%description Khmer
Khmer language support for KDE

%package Korean
Summary: Korean language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ko = %{version}-%{release}

%description Korean
Korean language support for KDE

%package Kurdish
Summary: Kurdish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ku = %{version}-%{release}

%description Kurdish
Kurdish language support for KDE

%package Lao
Summary: Lao language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-lo = %{version}-%{release}

%description Lao
Lao language support for KDE

%package Lithuanian
Summary: Lithuanian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-lt = %{version}-%{release}

%description Lithuanian
Lithuanian language support for KDE

%package Latvian
Summary: Latvian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-lv = %{version}-%{release}

%description Latvian
Latvian language support for KDE

%package LowSaxon
Summary: Low Saxon language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-nds = %{version}-%{release}

%description LowSaxon
Low Saxon language support for KDE

%package Maori
Summary: Maori language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-mi = %{version}-%{release}

%description Maori
Maori language support for KDE

%package Macedonian
Summary: Macedonian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-mk = %{version}-%{release}

%description Macedonian
Macedonian language support for KDE

%package Maithili
Summary: Maithili language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-mai = %{version}-%{release}

%description Maithili
Maithili language support for KDE

%package Malayalam
Summary: Malayalam language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ml = %{version}-%{release}

%description Malayalam
Malayalam language support for KDE

%package Maltese
Summary: Maltese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-mt = %{version}-%{release}

%description Maltese
Maltese language support for KDE

%package Marathi
Summary: Marathi language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-mr = %{version}-%{release}

%description Marathi
Marathi language support for KDE

%package Nepali
Summary: Nepali language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ne = %{version}-%{release}

%description Nepali
Nepali language support for KDE

%package Dutch
Summary: Dutch language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-nl = %{version}-%{release}

%description Dutch
Dutch language support for KDE

%package NorthernSami
Summary: Northern Sami language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-se = %{version}-%{release}

%description NorthernSami
Northern Sami language support for KDE

%package Norwegian
Summary: Norwegian (Bokmaal) language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-no = %{version}-%{release}

%description Norwegian
Norwegian (Bokmaal) language support for KDE

%package Norwegian-Nynorsk
Summary: Norwegian (Nynorsk) language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-nn = %{version}-%{release}

%description Norwegian-Nynorsk
Norwegian (Nynorsk) language support for KDE

%package Occitan
Summary: Occitan language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-oc = %{version}-%{release}

%description Occitan
Occitan language support for KDE

%package Polish
Summary: Polish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-pl = %{version}-%{release}

%description Polish
Polish language support for KDE

%package Portuguese
Summary: Portuguese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-pt = %{version}-%{release}

%description Portuguese
Portuguese language support for KDE

%package Punjabi
Summary: Punjabi language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-pa = %{version}-%{release}

%description Punjabi
Punjabi language support for KDE

%package Brazil
Summary: Brazil Portuguese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-pt_BR = %{version}-%{release}

%description Brazil
Brazil Portuguese language support for KDE

%package Romanian
Summary: Romanian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ro = %{version}-%{release}

%description Romanian
Romanian language support for KDE

%package Russian
Summary: Russian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ru = %{version}-%{release}

%description Russian
Russian language support for KDE

%package Slovak
Summary: Slovak language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-sk = %{version}-%{release}

%description Slovak
Slovak language support for KDE

%package Slovenian
Summary: Slovenian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-sl = %{version}-%{release}

%description Slovenian
Slovenian language support for KDE

%package Serbian
Summary: Serbian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-sr = %{version}-%{release}

%description Serbian
Serbian language support for KDE

%package Swedish
Summary: Swedish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-sv = %{version}-%{release}

%description Swedish
Swedish language support for KDE

%package Tamil
Summary: Tamil language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ta = %{version}-%{release}

%description Tamil
Tamil language support for KDE

%package Tajik
Summary: Tajik language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-tg = %{version}-%{release}

%description Tajik
Tajik language support for KDE

%package Thai
Summary: Thai language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-th = %{version}-%{release}

%description Thai
Thai language support for KDE

%package Turkish
Summary: Turkish language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-tr = %{version}-%{release}

%description Turkish
Turkish language support for KDE

%package Ukrainian
Summary: Ukrainian language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-uk = %{version}-%{release}

%description Ukrainian
Ukrainian language support for KDE

%package Venda
Summary: Venda language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-ven = %{version}-%{release}

%description Venda
Venda language support for KDE

%package Vietnamese
Summary: Vietnamese language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-vi = %{version}-%{release}

%description Vietnamese
Vietnamese language support for KDE

%package Walloon
Summary: Walloon language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-wa = %{version}-%{release}

%description Walloon
Walloon language support for KDE

%package Xhosa
Summary: Xhosa (a Bantu language) support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-xh = %{version}-%{release}

%description Xhosa
Xhosa (a Bantu language) support for KDE

%package Chinese
Summary: Chinese (Simplified Chinese) language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-zh_CN = %{version}-%{release}

%description Chinese
Chinese (Simplified Chinese) language support for KDE

%package Chinese-Traditional
Summary: Chinese (Traditional) language support for KDE
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: %{name}-zh_TW = %{version}-%{release}

%description Chinese-Traditional
Chinese (Traditional) language support for KDE

%prep
%setup -q -n %{name}-%{version} -c -a 0 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 11 -a 12 -a 13 -a 14 -a 15 -a 16 -a 17 -a 18 -a 19 -a 20 -a 21 -a 22 -a 23 -a 24 -a 25 -a 26 -a 27 -a 28 -a 29 -a 30 -a 32 -a 33 -a 34 -a 35 -a 36 -a 37 -a 38 -a 40 -a 41 -a 42 -a 44 -a 45 -a 46 -a 47 -a 48 -a 49 -a 50 -a 51 -a 52 -a 53 -a 54 -a 55 -a 56 -a 57 -a 58 -a 59 -a 60 -a 61 -a 62 -a 63

# upstream patches

%build
for i in $(cat %{SOURCE1000}) ; do
  pushd %{name}-$i-%{version}
  # skip kdewebdev for now, because we're still shipping kdewebdev 3 due to Quanta
  sed -i -e 's/add_subdirectory( *kdewebdev *)/#add_subdirectory(kdewebdev)/g' messages/CMakeLists.txt
  if [ -e docs/CMakeLists.txt ] ; then
    sed -i -e 's/add_subdirectory( *kdewebdev *)/#add_subdirectory(kdewebdev)/g' docs/CMakeLists.txt
  fi
  # remove lilo-config, conflicts with 3.5.9
  rm -f messages/kdeadmin/kcmlilo.po
  if [ -e docs/kdeadmin/CMakeLists.txt ] ; then
    sed -i -e 's/add_subdirectory( *lilo-config *)/#add_subdirectory(lilo-config)/g' docs/kdeadmin/CMakeLists.txt
  fi
  # remove bogus duplicated kdepim stuff from kdenetwork
  if [ -e docs/kdenetwork/CMakeLists.txt ] ; then
    sed -i -e 's/add_subdirectory( *korn *)/#add_subdirectory(korn)/g' -e 's/add_subdirectory( *kmail *)/#add_subdirectory(kmail)/g' -e 's/add_subdirectory( *knode *)/#add_subdirectory(knode)/g' docs/kdenetwork/CMakeLists.txt
  fi
  mkdir -p %{_target_platform}
  pushd %{_target_platform}
  %{cmake_kde4} ..
  popd
  popd
done

%install
rm -rf %{buildroot}

for i in $(cat %{SOURCE1000}) ; do
  make -C %{name}-$i-%{version}/%{_target_platform} DESTDIR=%{buildroot} install
done

# get rid of flags
rm -f %{buildroot}%{_datadir}/locale/*/flag.png

# get rid of documentation for apps which have been dropped from KDE 4
rm -rf %{buildroot}%{_kde4_docdir}/HTML/*/aktion
rm -rf %{buildroot}%{_kde4_docdir}/HTML/*/flashkard
rm -rf %{buildroot}%{_kde4_docdir}/HTML/*/kdvi
rm -rf %{buildroot}%{_kde4_docdir}/HTML/*/kedit
rm -rf %{buildroot}%{_kde4_docdir}/HTML/*/kmathtool
rm -rf %{buildroot}%{_kde4_docdir}/HTML/*/krec
rm -rf %{buildroot}%{_kde4_docdir}/HTML/*/ksirc
rm -rf %{buildroot}%{_kde4_docdir}/HTML/*/ksirtet
rm -rf %{buildroot}%{_kde4_docdir}/HTML/*/ksmiletris
rm -rf %{buildroot}%{_kde4_docdir}/HTML/*/ksplashml

%clean
rm -rf %{buildroot}


%files
# empty

%if %{buildall}
%files Afrikaans
%defattr(-,root,root)
%lang(af) %{_datadir}/locale/af/LC_MESSAGES/*
%lang(af) %{_datadir}/locale/af/entry.desktop
%endif

%files Arabic
%defattr(-,root,root)
%lang(ar) %{_datadir}/locale/ar/LC_MESSAGES/*
%lang(ar) %{_datadir}/locale/ar/entry.desktop
%lang(ar) %{_datadir}/locale/ar/LC_SCRIPTS/
%lang(ar) %{_datadir}/kde4/apps/klettres/ar

%if %{buildall}
%files Azerbaijani
%defattr(-,root,root)
%lang(az) %{_datadir}/locale/az/LC_MESSAGES/*
%lang(az) %{_datadir}/locale/az/entry.desktop
%endif

%if %{buildall}
%files Belarusian
%defattr(-,root,root)
%lang(be) %{_datadir}/locale/be/LC_MESSAGES/*
%lang(be) %{_datadir}/locale/be/entry.desktop
%endif

%files Bulgarian
%defattr(-,root,root)
%lang(bg) %{_datadir}/locale/bg/LC_MESSAGES/*
%lang(bg) %{_datadir}/locale/bg/entry.desktop
%lang(bg) %{_kde4_appsdir}/kvtml/bg

%files Bengali-India
%defattr(-,root,root)
%lang(bn_IN) %{_datadir}/locale/bn_IN/LC_MESSAGES/*
%lang(bn_IN) %{_datadir}/locale/bn_IN/entry.desktop

%if %{buildall}
%files Tibetan
%defattr(-,root,root)
%lang(bo) %{_datadir}/locale/bo/LC_MESSAGES/*
%lang(bo) %{_datadir}/locale/bo/entry.desktop
%endif

%if %{buildall}
%files Breton
%defattr(-,root,root)
%lang(br) %{_datadir}/locale/br/LC_MESSAGES/*
%lang(br) %{_datadir}/locale/br/entry.desktop
%endif

%if %{buildall}
%files Bosnian
%defattr(-,root,root)
%lang(bs) %{_datadir}/locale/bs/LC_MESSAGES/*
%lang(bs) %{_datadir}/locale/bs/entry.desktop
%endif

%files Catalan
%defattr(-,root,root)
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/*
%lang(ca) %{_datadir}/locale/ca/LC_SCRIPTS/
%lang(ca) %{_datadir}/locale/ca/entry.desktop
%lang(ca) %{_kde4_appsdir}/khangman/ca.txt
%lang(ca) %{_kde4_appsdir}/ktuberling/sounds/ca*
%lang(ca) %{_kde4_appsdir}/kvtml/ca
%lang(ca) %{_kde4_appsdir}/kvtml/latinCatalan*
%lang(ca) %{_kde4_docdir}/HTML/ca
%lang(ca) %{_mandir}/ca/*/*

%files Czech
%defattr(-,root,root)
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/*
%lang(cs) %{_datadir}/locale/cs/entry.desktop
%lang(cs) %{_kde4_appsdir}/khangman/cs.txt
%lang(cs) %{_kde4_appsdir}/klettres/cs
%lang(cs) %{_kde4_appsdir}/kvtml/cs
%lang(cs) %{_kde4_docdir}/HTML/cs

%if %{buildall}
%files Welsh
%defattr(-,root,root)
%lang(cy) %{_datadir}/locale/cy/LC_MESSAGES/*
%lang(cy) %{_datadir}/locale/cy/entry.desktop
%endif

%files Danish
%defattr(-,root,root)
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/*
%lang(da) %{_datadir}/locale/da/entry.desktop
%lang(da) %{_kde4_appsdir}/ktuberling/sounds/da*
%lang(da) %{_kde4_appsdir}/khangman/da.txt
%lang(da) %{_kde4_appsdir}/klettres/da
%lang(da) %{_kde4_appsdir}/kvtml/da
%lang(da) %{_kde4_docdir}/HTML/da
%lang(da) %{_mandir}/da/*/*

%files German
%defattr(-,root,root)
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/*
%lang(de) %{_datadir}/locale/de/LC_SCRIPTS/
%lang(de) %{_datadir}/locale/de/entry.desktop
%lang(de) %{_kde4_appsdir}/klettres/de
%lang(de) %{_kde4_appsdir}/ktuberling/sounds/de*
%lang(de) %{_kde4_appsdir}/khangman/de.txt
%lang(de) %{_kde4_appsdir}/kvtml/de
%lang(de) %{_kde4_appsdir}/step/objinfo/l10n/de/
%lang(de) %{_kde4_docdir}/HTML/de
%lang(de) %{_mandir}/de/*/*

%files Greek
%defattr(-,root,root)
%lang(el) %{_datadir}/locale/el/LC_MESSAGES/*
%lang(el) %{_datadir}/locale/el/entry.desktop
%lang(el) %{_kde4_appsdir}/kvtml/el

%files Gujarati
%defattr(-,root,root)
%lang(gu) %{_datadir}/locale/gu/LC_MESSAGES/*
%lang(gu) %{_datadir}/locale/gu/entry.desktop

%files British
%defattr(-,root,root)
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/*
%lang(en_GB) %{_datadir}/locale/en_GB/entry.desktop
%lang(en_GB) %{_kde4_appsdir}/klettres/en_GB
%lang(en_GB) %{_kde4_appsdir}/kvtml/en_GB
%lang(en_GB) %{_kde4_docdir}/HTML/en_GB
%lang(en_GB) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.en_GB.xml
%lang(en_GB) %{_kde4_appsdir}/kturtle/data/logokeywords.en_GB.xml
%lang(en_GB) %{_kde4_appsdir}/kturtle/examples/en_GB/*.logo

%if %{buildall}
%files Esperanto
%defattr(-,root,root)
%lang(eo) %{_datadir}/locale/eo/LC_MESSAGES/*
%lang(eo) %{_datadir}/locale/eo/entry.desktop
%endif

%files Spanish
%defattr(-,root,root)
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/*
%lang(es) %{_datadir}/locale/es/entry.desktop
%lang(es) %{_kde4_appsdir}/ktuberling/sounds/es*
%lang(es) %{_kde4_appsdir}/khangman/es.txt
%lang(es) %{_kde4_appsdir}/klettres/es
%lang(es) %{_kde4_appsdir}/kvtml/es
%lang(es) %{_kde4_docdir}/HTML/es
%lang(es) %{_mandir}/es/*/*

%files Estonian
%defattr(-,root,root)
%lang(et) %{_datadir}/locale/et/LC_MESSAGES/*
%lang(et) %{_datadir}/locale/et/entry.desktop
%lang(et) %{_kde4_appsdir}/khangman/et.txt
%lang(et) %{_kde4_appsdir}/kvtml/et
%lang(et) %{_kde4_docdir}/HTML/et
%lang(et) %{_mandir}/et/*/*

%files Basque
%defattr(-,root,root)
%lang(eu) %{_datadir}/locale/eu/LC_MESSAGES/*
%lang(eu) %{_datadir}/locale/eu/entry.desktop
%lang(eu) %{_kde4_docdir}/HTML/eu

%if %{buildall}
%files Farsi
%defattr(-,root,root)
%lang(fa) %{_datadir}/locale/fa/LC_MESSAGES/*
%lang(fa) %{_datadir}/locale/fa/entry.desktop
%endif

%files Finnish
%defattr(-,root,root)
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/*
%lang(fi) %{_datadir}/locale/fi/entry.desktop
%lang(fi) %{_kde4_appsdir}/khangman/fi.txt
%lang(fi) %{_kde4_appsdir}/ktuberling/sounds/fi*
%lang(fi) %{_kde4_appsdir}/kvtml/fi

%if %{buildall}
%files Faroese
%defattr(-,root,root)
%lang(fo) %{_datadir}/locale/fo/LC_MESSAGES/*
%lang(fo) %{_datadir}/locale/fo/entry.desktop
%endif

%files French
%defattr(-,root,root)
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/*
%lang(fr) %{_datadir}/locale/fr/entry.desktop
%lang(fr) %{_kde4_appsdir}/ktuberling/sounds/fr*
%lang(fr) %{_kde4_appsdir}/khangman/fr.txt
%lang(fr) %{_kde4_appsdir}/kvtml/fr
%lang(fr) %{_kde4_docdir}/HTML/fr
%lang(fr) %{_mandir}/fr/*/*

%files Frisian
%defattr(-,root,root)
%lang(fy) %{_datadir}/locale/fy/LC_MESSAGES/*
%lang(fy) %{_datadir}/locale/fy/entry.desktop

%files Irish
%defattr(-,root,root)
%lang(ga) %{_datadir}/locale/ga/LC_MESSAGES/*
%lang(ga) %{_datadir}/locale/ga/LC_SCRIPTS/
%lang(ga) %{_datadir}/locale/ga/entry.desktop
%lang(ga) %{_kde4_appsdir}/khangman/ga.txt
%lang(ga) %{_kde4_appsdir}/ktuberling/sounds/ga*
%lang(ga) %{_kde4_appsdir}/kvtml/ga

%files Galician
%defattr(-,root,root)
%lang(gl) %{_datadir}/locale/gl/LC_MESSAGES/*
%lang(gl) %{_datadir}/locale/gl/entry.desktop
%lang(gl) %{_kde4_appsdir}/kvtml/gl
%lang(gl) %{_kde4_appsdir}/ktuberling/sounds/gl.soundtheme
%lang(gl) %{_kde4_appsdir}/ktuberling/sounds/gl/
%lang(gl) %{_kde4_docdir}/HTML/gl
%lang(gl) %{_mandir}/gl/*/*

%files Hebrew
%defattr(-,root,root)
%lang(he) %{_datadir}/locale/he/LC_MESSAGES/*
%lang(he) %{_datadir}/locale/he/entry.desktop
%lang(he) %{_kde4_appsdir}/klettres/he
%lang(he) %{_kde4_docdir}/HTML/he

%files Hindi
%defattr(-,root,root)
%lang(hi) %{_datadir}/locale/hi/LC_MESSAGES/*
%lang(hi) %{_datadir}/locale/hi/entry.desktop

%files Chhattisgarhi
%defattr(-,root,root,-)
%lang(hne) %{_datadir}/locale/hne/LC_MESSAGES/*
%lang(hne) %{_datadir}/locale/hne/entry.desktop


%files Croatian
%defattr(-,root,root)
%lang(hr) %{_datadir}/locale/hr/LC_MESSAGES/*
%lang(hr) %{_datadir}/locale/hr/entry.desktop
%lang(hr) %{_datadir}/locale/hr/LC_SCRIPTS

%files Hungarian
%defattr(-,root,root)
%lang(hu) %{_datadir}/locale/hu/LC_MESSAGES/*
%lang(hu) %{_datadir}/locale/hu/entry.desktop
%lang(hu) %{_kde4_appsdir}/khangman/hu.txt
%lang(hu) %{_kde4_appsdir}/kvtml/hu
%lang(hu) %{_kde4_appsdir}/klettres/hu
%lang(hu) %{_kde4_docdir}/HTML/hu

%if %{buildall}
%files Indonesian
%defattr(-,root,root)
%lang(id) %{_datadir}/locale/id/LC_MESSAGES/*
%lang(id) %{_datadir}/locale/id/entry.desktop
%endif

%files Icelandic
%defattr(-,root,root)
%lang(is) %{_datadir}/locale/is/LC_MESSAGES/*
%lang(is) %{_datadir}/locale/is/entry.desktop

%files Italian
%defattr(-,root,root)
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/*
%lang(it) %{_datadir}/locale/it/entry.desktop
%lang(it) %{_kde4_appsdir}/ktuberling/sounds/it*
%lang(it) %{_kde4_appsdir}/klettres/it
%lang(it) %{_kde4_appsdir}/kvtml/it
%lang(it) %{_kde4_docdir}/HTML/it
%lang(it) %{_kde4_appsdir}/step/objinfo/l10n/it/
%lang(it) %{_mandir}/it/*/*

%files Japanese
%defattr(-,root,root)
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/*
%lang(ja) %{_datadir}/locale/ja/LC_SCRIPTS/
%lang(ja) %{_datadir}/locale/ja/entry.desktop
%lang(ja) %{_kde4_docdir}/HTML/ja

%files Kannada
%defattr(-,root,root)
%lang(kn) %{_datadir}/locale/kn/LC_MESSAGES/*
%lang(kn) %{_datadir}/locale/kn/entry.desktop

%files Kashubian
%defattr(-,root,root)
%lang(csb) %{_datadir}/locale/csb/LC_MESSAGES/*
%lang(csb) %{_datadir}/locale/csb/entry.desktop

%files Kazakh
%defattr(-,root,root)
%lang(kk) %{_datadir}/locale/kk/LC_MESSAGES/*
%lang(kk) %{_datadir}/locale/kk/entry.desktop

%files Khmer
%defattr(-,root,root)
%lang(km) %{_datadir}/locale/km/LC_MESSAGES/*
%lang(km) %{_datadir}/locale/km/entry.desktop

%files Korean
%defattr(-,root,root)
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/*
%lang(ko) %{_datadir}/locale/ko/LC_SCRIPTS/
%lang(ko) %{_datadir}/locale/ko/entry.desktop
%lang(ko) %{_kde4_docdir}/HTML/ko/

%files Kurdish
%defattr(-,root,root)
%lang(ku) %{_datadir}/locale/ku/LC_MESSAGES/*
%lang(ku) %{_datadir}/locale/ku/entry.desktop

%if %{buildall}
%files Lao
%defattr(-,root,root)
%lang(lo) %{_datadir}/locale/lo/LC_MESSAGES/*
%lang(lo) %{_datadir}/locale/lo/entry.desktop
%endif

%files Lithuanian
%defattr(-,root,root)
%lang(lt) %{_datadir}/locale/lt/LC_MESSAGES/*
%lang(lt) %{_datadir}/locale/lt/entry.desktop
%lang(lt) %{_kde4_docdir}/HTML/lt/

%files LowSaxon
%defattr(-,root,root)
%lang(nds) %{_datadir}/locale/nds/LC_MESSAGES/*
%lang(nds) %{_datadir}/locale/nds/entry.desktop
%lang(nds) %{_kde4_appsdir}/klettres/nds
%lang(nds) %{_kde4_appsdir}/khangman/nds.txt
%lang(nds) %{_kde4_appsdir}/kvtml/nds
%lang(nds) %{_kde4_appsdir}/ktuberling/sounds/nds*
%lang(nds) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.nds.xml
%lang(nds) %{_kde4_appsdir}/kturtle/examples/nds
%lang(nds) %{_kde4_docdir}/HTML/nds

%files Latvian
%defattr(-,root,root)
%lang(lv) %{_datadir}/locale/lv/LC_MESSAGES/*
%lang(lv) %{_datadir}/locale/lv/entry.desktop

%if %{buildall}
%files Maori
%defattr(-,root,root)
%lang(mi) %{_datadir}/locale/mi/LC_MESSAGES/*
%lang(mi) %{_datadir}/locale/mi/entry.desktop
%endif

%files Macedonian
%defattr(-,root,root)
%lang(mk) %{_datadir}/locale/mk/LC_MESSAGES/*
%lang(mk) %{_datadir}/locale/mk/entry.desktop

%files Maithili
%defattr(-,root,root)
%lang(mai) %{_datadir}/locale/mai/LC_MESSAGES/*
%lang(mai) %{_datadir}/locale/mai/entry.desktop

%files Marathi
%defattr(-,root,root)
%lang(mr) %{_datadir}/locale/mr/LC_MESSAGES/*
%lang(mr) %{_datadir}/locale/mr/entry.desktop

%files Malayalam
%defattr(-,root,root)
%lang(ml) %{_datadir}/locale/ml/LC_MESSAGES/*
%lang(ml) %{_datadir}/locale/ml/LC_SCRIPTS/
%lang(ml) %{_datadir}/locale/ml/entry.desktop
%lang(ml) %{_kde4_appsdir}/klettres/ml/

%if %{buildall}
%files Maltese
%defattr(-,root,root)
%lang(mt) %{_datadir}/locale/mt/LC_MESSAGES/*
%lang(mt) %{_datadir}/locale/mt/entry.desktop
%endif

%if %{buildall}
%files Nepali
%defattr(-,root,root)
%lang(ne) %{_datadir}/locale/ne/LC_MESSAGES/*
%lang(ne) %{_datadir}/locale/ne/entry.desktop
%endif

%files Dutch
%defattr(-,root,root)
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/*
%lang(nl) %{_datadir}/locale/nl/LC_SCRIPTS/
%lang(nl) %{_datadir}/locale/nl/entry.desktop
%lang(nl) %{_kde4_appsdir}/ktuberling/sounds/nl*
%lang(nl) %{_kde4_appsdir}/klettres/nl
%lang(nl) %{_kde4_appsdir}/kvtml/nl
%lang(nl) %{_kde4_docdir}/HTML/nl
%lang(nl) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.nl.xml
%lang(nl) %{_kde4_appsdir}/kturtle/data/logokeywords.nl.xml
%lang(nl) %{_kde4_appsdir}/kturtle/examples/nl/*.logo
%lang(nl) %{_mandir}/nl/*/*

%if %{buildall}
%files NorthernSami
%defattr(-,root,root)
%lang(se) %{_datadir}/locale/se/LC_MESSAGES/*
%lang(se) %{_datadir}/locale/se/entry.desktop
%endif

%files Norwegian
%defattr(-,root,root)
%lang(nb) %{_datadir}/locale/nb/LC_MESSAGES/*
%lang(nb) %{_datadir}/locale/nb/LC_SCRIPTS/
%lang(nb) %{_datadir}/locale/nb/entry.desktop
%lang(nb) %{_kde4_appsdir}/khangman/nb.txt
%lang(nb) %{_kde4_appsdir}/kvtml/nb/
%lang(nb) %{_kde4_docdir}/HTML/nb/
%lang(nb) %{_kde4_appsdir}/klettres/nb
%lang(nb) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.nb.xml
%lang(nb) %{_kde4_appsdir}/kturtle/data/logokeywords.nb.xml
%lang(nb) %{_kde4_appsdir}/kturtle/examples/nb/*.logo
%lang(nb) %{_mandir}/nb/*/*

%files Norwegian-Nynorsk
%defattr(-,root,root)
%lang(nn) %{_datadir}/locale/nn/LC_MESSAGES/*
%lang(nn) %{_datadir}/locale/nn/LC_SCRIPTS/
%lang(nn) %{_datadir}/locale/nn/entry.desktop
%lang(nn) %{_kde4_appsdir}/khangman/nn.txt
%lang(nn) %{_kde4_appsdir}/kvtml/nn/
%lang(nn) %{_kde4_docdir}/HTML/nn
%lang(nn) %{_mandir}/nn/*/*

%if %{buildall}
%files Occitan
%defattr(-,root,root)
%lang(oc) %{_datadir}/locale/oc/LC_MESSAGES/*
%lang(oc) %{_datadir}/locale/oc/entry.desktop
%endif

%files Punjabi
%defattr(-,root,root)
%lang(pa) %{_datadir}/locale/pa/LC_MESSAGES/*
%lang(pa) %{_datadir}/locale/pa/entry.desktop

%files Polish
%defattr(-,root,root)
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/*
%lang(pl) %{_datadir}/locale/pl/LC_SCRIPTS/
%lang(pl) %{_datadir}/locale/pl/entry.desktop
%lang(pl) %{_kde4_appsdir}/khangman/pl.txt
%lang(pl) %{_kde4_appsdir}/kvtml/pl
%lang(pl) %{_kde4_docdir}/HTML/pl
%lang(pl) %{_mandir}/pl/*/*

%files Portuguese
%defattr(-,root,root)
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/*
%lang(pt) %{_datadir}/locale/pt/entry.desktop
%lang(pt) %{_kde4_appsdir}/khangman/pt.txt
%lang(pt) %{_kde4_appsdir}/ktuberling/sounds/pt*
%lang(pt) %{_kde4_appsdir}/kvtml/pt
%lang(pt) %{_kde4_docdir}/HTML/pt
%lang(pt) %{_mandir}/pt/*/*

%files Brazil
%defattr(-,root,root)
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/*
%lang(pt_BR) %{_datadir}/locale/pt_BR/entry.desktop
%lang(pt_BR) %{_kde4_appsdir}/khangman/pt_BR.txt
%lang(pt_BR) %{_kde4_appsdir}/klettres/pt_BR/*
%lang(pt_BR) %{_kde4_appsdir}/kvtml/pt_BR
%lang(pt_BR) %{_kde4_docdir}/HTML/pt_BR
%lang(pt_BR) %{_mandir}/pt_BR/*/*

%files Romanian
%defattr(-,root,root)
%lang(ro) %{_datadir}/locale/ro/LC_MESSAGES/*
%lang(ro) %{_datadir}/locale/ro/entry.desktop
%lang(ro) %{_kde4_appsdir}/kvtml/ro
%lang(ro) %{_kde4_appsdir}/ktuberling/sounds/ro*
%lang(ro) %{_kde4_docdir}/HTML/ro

%files Russian
%defattr(-,root,root)
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/*
%lang(ru) %{_datadir}/locale/ru/entry.desktop
%lang(ru) %{_kde4_appsdir}/kvtml/ru
%lang(ru) %{_kde4_docdir}/HTML/ru
%lang(ru) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.ru.xml
%lang(ru) %{_kde4_appsdir}/kturtle/data/logokeywords.ru.xml
%lang(ru) %{_kde4_appsdir}/kturtle/examples/ru/*.logo
%lang(ru) %{_mandir}/ru/*/*

%files Slovak
%defattr(-,root,root)
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/*
%lang(sk) %{_datadir}/locale/sk/entry.desktop
#%lang(sk) %{_kde4_appsdir}/ktuberling/sounds/sk*
#%lang(sk) %{_kde4_appsdir}/klettres/sk

%files Slovenian
%defattr(-,root,root)
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/*
%lang(sl) %{_datadir}/locale/sl/entry.desktop
%lang(sl) %{_kde4_appsdir}/ktuberling/sounds/sl*
%lang(sl) %{_kde4_appsdir}/khangman/sl.txt
%lang(sl) %{_kde4_appsdir}/kvtml/sl
%lang(sl) %{_kde4_appsdir}/katepart/syntax/logohighlightstyle.sl.xml
%lang(sl) %{_kde4_appsdir}/kturtle/data/logokeywords.sl.xml
%lang(sl) %{_kde4_appsdir}/kturtle/examples/sl/*.logo
%lang(sl) %{_kde4_docdir}/HTML/sl

%files Serbian
%defattr(-,root,root)
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/*
%lang(sr) %{_datadir}/locale/sr/LC_SCRIPTS/
%lang(sr) %{_datadir}/locale/sr/entry.desktop
%lang(sr) %{_kde4_appsdir}/ktuberling/sounds/sr*
%lang(sr) %{_kde4_docdir}/HTML/sr
%lang(sr) %{_kde4_docdir}/HTML/sr@latin
%lang(sr) %{_kde4_iconsdir}/*/*/*/*/sr/*
%lang(sr) %{_kde4_iconsdir}/*/*/*/*/sr@latin/*
%lang(sr) %{_kde4_appsdir}/desktoptheme/*/widgets/l10n/sr
%lang(sr) %{_kde4_appsdir}/desktoptheme/*/widgets/l10n/sr@latin
%lang(sr) %{_kde4_appsdir}/khangman/sr@latin.txt
%lang(sr) %{_kde4_appsdir}/kvtml/sr*
%lang(sr) %{_datadir}/locale/sr@latin/LC_MESSAGES/*
%lang(sr) %{_datadir}/locale/sr@latin/entry.desktop
%lang(sr) %{_mandir}/sr/*/*
%lang(sr) %{_mandir}/sr@latin/*/*

%files Swedish
%defattr(-,root,root)
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/*
%lang(sv) %{_datadir}/locale/sv/entry.desktop
%lang(sv) %{_datadir}/locale/sv/LC_SCRIPTS/
%lang(sv) %{_kde4_appsdir}/ktuberling/sounds/sv*
%lang(sv) %{_kde4_appsdir}/khangman/sv.txt
%lang(sv) %{_kde4_appsdir}/kvtml/sv
%lang(sv) %{_kde4_docdir}/HTML/sv
%lang(sv) %{_mandir}/sv/*/*

%if %{buildall}
%files Tamil
%defattr(-,root,root)
%lang(ta) %{_datadir}/locale/ta/LC_MESSAGES/*
%lang(ta) %{_datadir}/locale/ta/entry.desktop
%endif

%files Tajik
%defattr(-,root,root)
%lang(tg) %{_datadir}/locale/tg/LC_MESSAGES/*
%lang(tg) %{_datadir}/locale/tg/entry.desktop
%lang(tg) %{_kde4_appsdir}/kvtml/tg
%lang(tg) %{_kde4_appsdir}/khangman/tg.txt

%files Thai
%defattr(-,root,root)
%lang(th) %{_datadir}/locale/th/LC_MESSAGES/*
%lang(th) %{_datadir}/locale/th/charset
%lang(th) %{_datadir}/locale/th/entry.desktop

%files Turkish
%defattr(-,root,root)
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/*
%lang(tr) %{_datadir}/locale/tr/entry.desktop
%lang(tr) %{_kde4_appsdir}/khangman/tr.txt
%lang(tr) %{_kde4_appsdir}/kvtml/tr
%lang(tr) %{_kde4_docdir}/HTML/tr

%files Ukrainian
%defattr(-,root,root)
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/*
%lang(uk) %{_datadir}/locale/uk/LC_SCRIPTS/
%lang(uk) %{_datadir}/locale/uk/entry.desktop
%lang(uk) %{_kde4_appsdir}/ktuberling/sounds/uk*
%lang(uk) %{_kde4_appsdir}/step/objinfo/l10n/uk/
%lang(uk) %{_kde4_appsdir}/kvtml/uk
%lang(uk) %{_kde4_docdir}/HTML/uk
%lang(uk) %{_mandir}/uk/*/*

%if %{buildall}
%files Venda
%defattr(-,root,root)
%lang(ven) %{_datadir}/locale/ven/LC_MESSAGES/*
%lang(ven) %{_datadir}/locale/ven/entry.desktop
%endif

%if %{buildall}
%files Vietnamese
%defattr(-,root,root)
%lang(vi) %{_datadir}/locale/vi/LC_MESSAGES/*
%lang(vi) %{_datadir}/locale/vi/entry.desktop
%endif

%files Walloon
%defattr(-,root,root)
%lang(wa) %{_datadir}/locale/wa/LC_MESSAGES/*
%lang(wa) %{_datadir}/locale/wa/entry.desktop
%lang(wa) %{_kde4_appsdir}/ktuberling/sounds/wa*
%lang(wa) %{_kde4_docdir}/HTML/wa

%if %{buildall}
%files Xhosa
%defattr(-,root,root)
%lang(xh) %{_datadir}/locale/xh/LC_MESSAGES/*
%lang(xh) %{_datadir}/locale/xh/entry.desktop
%endif

%files Chinese
%defattr(-,root,root)
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/*
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_SCRIPTS/
%lang(zh_CN) %{_datadir}/locale/zh_CN/charset
%lang(zh_CN) %{_datadir}/locale/zh_CN/entry.desktop
%lang(zh_CN) %{_kde4_appsdir}/kvtml/zh_CN
%lang(zh_CN) %{_kde4_appsdir}/step/objinfo/l10n/zh_CN/
%lang(zh_CN) %{_kde4_docdir}/HTML/zh_CN

%files Chinese-Traditional
%defattr(-,root,root)
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/*
%lang(zh_TW) %{_datadir}/locale/zh_TW/entry.desktop
%lang(zh_TW) %{_kde4_docdir}/HTML/zh_TW


%changelog
* Thu Jan 07 2010 Than Ngo <than@redhat.com> - 4.3.4-5
- fix url

* Fri Dec 18 2009 Than Ngo <than@redhat.com> - 4.3.4-4
- don't use RPM_SOURCE_DIR to unpack source

* Fri Dec 18 2009 Than Ngo <than@redhat.com> - 4.3.4-3
- clean

* Fri Dec 18 2009 Than Ngo <than@redhat.com> - 4.3.4-2
- fix url

* Tue Dec 01 2009 Than Ngo <than@redhat.com> - 4.3.4-1
- 4.3.4

* Fri Nov 13 2009 Than Ngo <than@redhat.com> - 4.3.3-2
- rhel cleanup, remove Fedora<=9 conditionals

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Oct 05 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Sat Oct 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.1-3
- main virtual subpkg

* Sat Sep 05 2009 Than Ngo <than@redhat.com> - 4.3.1-2
- add missing Croatian localization

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Tue Jul 14 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Tue Jul  7 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 4.2.95-2
- fix duplicate directory ownership (/usr/share/locale/*/LC_MESSAGES)

* Tue Jun 30 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Tue May 19 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.85-1
- KDE 4.3 beta 1

* Tue Mar 31 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-1
- KDE 4.2.2

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 4.2.1-1
- 4.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 30 2009 Than Ngo <than@redhat.com> - 4.2.0-2
- enable he

* Thu Jan 22 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Sat Jan 10 2009 Than Ngo <than@redhat.com> - 4.1.96-2
- remove debug

* Wed Jan 07 2009 Than Ngo <than@redhat.com> - 4.1.96-1
- 4.2rc1

* Fri Dec 12 2008 Than Ngo <than@redhat.com> - 4.1.85-1
- 4.2beta2

* Fri Nov 21 2008 Than Ngo <than@redhat.com> 4.1.80-1
- 4.2 beta1

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- 4.1.2
- reenable Kurdish, Lithuanian, Malayalam 

* Wed Sep 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.1-2
- reenable Frisian and Kazakh

* Fri Aug 29 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Tue Jul 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-2
- get rid of kdepim documentation from kdenetwork

* Sun Jul 27 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-1.2
- file conflict between kde-l10n and libkdcraw (#456797)

* Sat Jul 26 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-1.1
- on F9, remove translations for kdepim apps we don't ship (#456745)

* Wed Jul 23 2008 Than Ngo <than@redhat.com> 4.1.0-1
- 4.1.0

* Tue Jul 22 2008 Than Ngo <than@redhat.com> 4.0.98-1
- 4.0.98 (4.1rc1)

* Sat Jun 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.83-2
- disable Serbian for now, it's broken
- fix file list for Ukranian

* Thu Jun 19 2008 Than Ngo <than@redhat.com> 4.0.83-1
- 4.0.83 (beta2)

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta 1

* Fri Apr 18 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-4
- remove documentation for apps which are not part of KDE 4.0

* Thu Apr 17 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-3
- disable kdewebdev documentation correctly

* Thu Apr 17 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- build documentation (#441537)
- mark Norvegian Bokmal translations with %%lang(nb) rather than %%lang(no)

* Tue Apr 01 2008 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3

* Mon Mar 03 2008 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2

* Thu Feb 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-3
- don't ship kdewebdev translations (we don't ship kdewebdev 4 yet)

* Thu Feb 07 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-2
- fix Danish not to include the data files for all languages
- include ktuberling sounds in the respective languages
- include kvtml (kanagram) translations in Czech

* Thu Jan 31 2008 Than Ngo <than@redhat.com> 4.0.1-1
- 4.0.1

* Fri Jan 18 2008 Lukas Tinkl <ltinkl@redhat.com> 4.0.0-4
- update languages for to the official KDE 4.0.0 list
- correct BR to kdelibs4-devel

* Fri Jan 18 2008 Lukas Tinkl <ltinkl@redhat.com> 4.0.0-2
- update languages for to the official KDE 4.0.0 list

* Wed Jan 09 2008 Than Ngo <than@redhat.com> 4.0.0-1
- 4.0.0

* Wed Dec 12 2007 Than Ngo <than@redhat.com> 3.97.0-1
- 3.97.0

* Tue Oct 16 2007 Than Ngo <than@redhat.com> 3.5.8-1
- 3.5.8

* Tue Feb 06 2007 Than Ngo <than@redhat.com> 1:3.5.6-1.fc7
- 3.5.6

* Tue Aug 08 2006 Than Ngo <than@redhat.com> 1:3.5.4-1
- 3.5.4

* Fri Jun 09 2006 Than Ngo <than@redhat.com> 1:3.5.3-3
- fix dangling symlinks

* Wed Jun 07 2006 Than Ngo <than@redhat.com> 1:3.5.3-2
- add BR on gettext-devel

* Sat Jun 03 2006 Than Ngo <than@redhat.com> 1:3.5.3-1
- update to 3.5.3

* Tue Apr 25 2006 Than Ngo <than@redhat.com> 1:3.5.2-3
- add kde-i18n-Lithuanian 

* Thu Apr 13 2006 Than Ngo <than@redhat.com> 1:3.5.2-2 
- fix file conflict

* Mon Apr 03 2006 Than Ngo <than@redhat.com> 1:3.5.2-1
- update to 3.5.2

* Wed Mar 08 2006 Than Ngo <than@redhat.com> 1:3.5.1-2 
- add missing zh_TW

* Wed Feb 01 2006 Than Ngo <than@redhat.com> 1:3.5.1-1
- 3.5.1

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 30 2005 Than Ngo <than@redhat.com> 1:3.5.0-1
- 3.5

* Thu Nov 03 2005 Than Ngo <than@redhat.com> 1:3.4.92-2
- add workaround for files conflict in Polish #171870

* Tue Oct 25 2005 Than Ngo <than@redhat.com> 1:3.4.92-1
- update to 3.5 beta2

* Mon Oct 10 2005 Than Ngo <than@redhat.com> 1:3.4.91-1
- update to 3.5 beta 1

* Thu Jul 21 2005 Than Ngo <than@redhat.com> 1:3.4.2-1
- 3.4.2

* Wed Jun 29 2005 Than Ngo <than@redhat.com> 1:3.4.1-1 
- 3.4.1

* Thu Mar 03 2005 Than Ngo <than@redhat.com> 1:3.4.0-0.rc1.2
- fix build problem

* Tue Mar 01 2005 Than Ngo <than@redhat.com> 1:3.4.0-0.rc1.1
- 3.4.0 rc1

* Sat Feb 19 2005 Than Ngo <than@redhat.com> 1:3.3.92-0.1
- KDE-3.4 beta2

* Sat Feb 12 2005 Than Ngo <than@redhat.com> 1:3.3.2-1 
- add Hindi, Tamil, Punjabi, Bengali translation

* Fri Dec 03 2004 Than Ngo <than@redhat.com> 1:3.3.2-0.1
- update to 3.3.2

* Sat Oct 16 2004 Than Ngo <than@redhat.com> 1:3.3.1-2
- rhel rebuilt

* Wed Oct 13 2004 Than Ngo <than@redhat.com> 1:3.3.1-1
- update to 3.3.1

* Tue Aug 31 2004 Than Ngo <than@redhat.com> 3.3.0-2
- fix rpm file list

* Mon Aug 23 2004 Than Ngo <than@redhat.com> 3.3.0-1
- update to 3.3.0

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 3.3.0-0.1.rc2
- update to 3.3.0 rc2
- add Bulgarian

* Fri Jun 18 2004 Than Ngo <than@redhat.com> 1:3.2.3-1 
- update to 3.2.3
- get rid of old brokon kde-i18n-ko
- add some new languages

* Tue Apr 20 2004 Than Ngo <than@redhat.com> 3.2.2-2
- add workaround for bug #121129, kdelibs conflicts with kde-i18n

* Tue Apr 13 2004 Than Ngo <than@redhat.com> 1:3.2.2-1
- 3.2.2 release

* Wed Mar 10 2004 Than Ngo <than@redhat.com> 1:3.2.1-2
- add missing Icelandic i18n

* Tue Mar 09 2004 Than Ngo <than@redhat.com> 1:3.2.1-1
- rebuild

* Fri Mar 05 2004 Than Ngo <than@redhat.com> 1:3.2.1-0.1
- 3.2.1 release

* Sun Feb 08 2004 Than Ngo <than@redhat.com> 1:3.2.0-0.2
- add missing kdevelop mo files

* Tue Feb 03 2004 Than Ngo <than@redhat.com> 1:3.2.0-0.1
- 3.2.0 release

* Mon Jan 19 2004 Than Ngo <than@redhat.com> 1:3.1.95-0.1
- KDE 3.2 RC1

* Thu Dec 11 2003 Than Ngo <than@redhat.com> 1:3.1.94-0.3
- fix rpm file list

* Thu Dec 04 2003 Than Ngo <than@redhat.com> 1:3.1.94-0.2
- add missing i18n for ko 

* Mon Dec 01 2003 Than Ngo <than@redhat.com> 1:3.1.94-0.1
- KDE 3.2 Beta2

* Sun Nov 09 2003 Than Ngo <than@redhat.com> 1:3.1.93-0.2
- fixed buildroot issue

* Wed Nov 05 2003 Than Ngo <than@redhat.com> 0.1:3.1.93-1
- 3.2 Beta 1

* Tue Sep 30 2003 Than Ngo <than@redhat.com> 1:3.1.4-1
- 3.1.4

* Sat Aug 02 2003 Than Ngo <than@redhat.com> 1:3.1.3-2
- rebuilt

* Sat Aug 02 2003 Than Ngo <than@redhat.com> 1:3.1.3-1
- rebuilt

* Mon Jul 21 2003 Than Ngo <than@redhat.com> 1:3.1.3-0.9x.2
- fix rpm file list

* Sun Jul 20 2003 Than Ngo <than@redhat.com> 1:3.1.3-0.9x.1
- 3.1.3

* Wed Jul 9 2003 Than Ngo <than@redhat.com> 1:3.1.2-4
- add some translation for kdesktop

* Mon May 19 2003 Than Ngo <than@redhat.com> 1:3.1.2-2
- 3.1.2

* Wed Mar 19 2003 Than Ngo <than@redhat.com> 1:3.1.1-1
- add ar/vi i18n
- fix typo bugs

* Wed Jan 29 2003 Than Ngo <than@redhat.com> 1:3.1-2
- fix conflict with kdevelop

* Tue Jan 28 2003 Than Ngo <than@redhat.com> 1:3.1-1
- 3.1 release
- fix #81724

* Mon Jan 27 2003 Than Ngo <than@redhat.com> 1:3.1-0.7
- rc7

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 1:3.1-0.6
- rebuild

* Mon Jan 13 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.5
- rc6
- exclude ia64

* Tue Dec 12 2002 Than Ngo <than@redhat.com> 3.1-0.4
- add missing requires kdelibs in sub packages

* Wed Dec 11 2002 Than Ngo <than@redhat.com> 3.1-0.3
- use %%configue
- dangling symlinks Bug #79345
- cleanup specfile

* Fri Nov 29 2002 Than Ngo <than@redhat.com> 3.1-0.2
- Add missing ko/is i18n

* Sun Nov 24 2002 Than Ngo <than@redhat.com> 3.1-0.1
- 3.1 rc4

* Sat Nov  9 2002 Than Ngo <than@redhat.com> 3.0.5-1
- 3.0.5

* Mon Oct 14 2002 Than Ngo <than@redhat.com> 3.0.4-1
- 3.0.4
- localiztion fix (bug #75085, #75012)

* Mon Aug 12 2002 Than Ngo <than@redhat.com> 3.0.3-1
- 3.0.3

* Tue Jul 09 2002 Than Ngo <than@redhat.com> 3.0.2-2
- get rid of zero-length files

* Tue Jul 09 2002 Than Ngo <than@redhat.com> 3.0.2-1
- 3.0.2

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 06 2002 Than Ngo <than@redhat.com> 3.0.1-1
- 3.0.1
- fixed rmplint errors #65989

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Apr 12 2002 Tim Powers <timp@redhat.com>3.0.0-5
- remove the following kde-i18n packages: Azerbaijani, Maltese,
  Esperanto, Tamil, Latvian, Xhosa, Lithuanian, Thai, and Bulgarian

* Tue Apr  9 2002 Than Ngo <than@redhat.com> 3.0.0-4
- fixed wrong tag 'nb' (bug #62890)

* Tue Apr  2 2002 Than Ngo <than@redhat.com> 3.0.0-3
- fixed Dangling Symlinks (#62559)

* Fri Mar 29 2002 Than Ngo <than@redhat.com> 3.0.0-2
- fix bug #61930
- add missing koffice-i18n

* Wed Mar 27 2002 Than Ngo <than@redhat.com> 3.0.0-1
- update kde 3.0 final

* Tue Mar 26 2002 Than Ngo <than@redhat.com> 3.0.0-0.cvs20020326.1
- update
- fix bug #61513

* Thu Mar 14 2002 Than Ngo <than@redhat.com> 3.0.0-0.cvs20020314.1
- update

* Mon Mar 10 2002 Than Ngo <than@redhat.com> 3.0.0-0.cvs20020310.1
- update
- enable i18n for koffice

* Tue Mar  6 2002 Than Ngo <than@redhat.com> 3.0.0-0.cvs20020306.1
- update
- enable Catalan i18n
- use zh_TW and zh_CN instead zh_TW.Big5 and zh_CN.GB2312 (bug #60759)
- get rid of Buildrequires arts-devel

* Tue Jan  8 2002 Than Ngo <than@redhat.com> 3.0.0-0.cvs20020108.1
- update to CVS
- fix some broken po files
- fixed specfile

* Tue Nov 20 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2.2-2
- Build all languages
- Add missing files

* Sun Nov 18 2001 Than Ngo <than@redhat.com> 2.2.2-1
- update to 2.2.2

* Tue Oct 09 2001 Than Ngo <than@redhat.com> 2.2-10
- fix rebuild problem against kdelibs-2.2-11 (bug #54476)

* Fri Sep 14 2001 Than Ngo <than@redhat.com> 2.2-9
- remove some broken stuff for building on s390

* Wed Aug 29 2001 Than Ngo <than@redhat.com> 2.2-8
- add some po files from Trond (Bug #35923, #35863)

* Thu Aug 23 2001 Than Ngo <than@redhat.com> 2.2-6
- add missing zh_TW.Big5
- fix file conflicts with koffice-i18n

* Tue Aug 14 2001 Tim Powers <timp@redhat.com>
- exclude Esperanto, Greek, Azerbaijani, Latvian, Maltese, Tamil,
  Serbian packages

* Tue Aug 14 2001 Than Ngo <than@redhat.com> 2.2-5
- add missing kde-i18n for Norway

* Mon Aug 13 2001 Than Ngo <than@redhat.com> 2.2-4
- fix dangling symlinks (bug #51647)

* Sun Aug 12 2001 Than Ngo <than@redhat.com> 2.2-3
- add korean i18n

* Fri Aug 10 2001 Than Ngo <than@redhat.com> 2.2-2
- many bug fixes

* Mon Aug  6 2001 Than Ngo <than@redhat.com> 2.2-1
- fix build dependency (bug #50463)
- fix some broken docbook

* Tue Jul 24 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010724.1
- update
- make symlinks relative

* Wed Feb 21 2001 Than Ngo <than@redhat.com>
- 2.1-respin

* Tue Feb 20 2001 Than Ngo <than@redhat.com>
- update to 2.1

* Mon Jan  1 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update

* Mon Nov 27 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to CVS

* Wed Nov  1 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to KDE_2_0_BRANCH

* Mon Oct 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.0 final

* Wed Oct  4 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- New CVS

* Thu Aug 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.93

* Sat Aug 19 2000 Than Ngo <than@redhat.com>
- put i18n stuff for KDE2 under /usr/lib/kde2,
  fix dependency problem

* Mon Jul 03 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- add default owner

* Sat Apr 15 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Initial RPM
