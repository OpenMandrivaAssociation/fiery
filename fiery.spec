#define snapshot 20220107

Name:		fiery
Version:	2.0.1
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	A convergent web browser for Maui
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/fiery/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/maui-%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/maui-%{name}-%{snapshot}.tar.bz2}
#Patch0:   https://invent.kde.org/maui/maui-fiery/-/commit/54a9e3cf7ef9fd99a95ffc489adeaaff015d6d90.patch
License:	GPLv3
Group:		Development/Tools
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:	gettext
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Widgets)

%description
A convergent web browser for Maui

%prep
%autosetup -p1 -n maui-%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang fiery

%files -f fiery.lang
%{_bindir}/fiery
%{_datadir}/applications/org.kde.fiery.desktop
%{_datadir}/metainfo/org.kde.fiery.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/fiery.svg
