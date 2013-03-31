Summary:	GNome Audio Converter
Name:		gnac
Version:	0.2.4.1
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://heanet.dl.sourceforge.net/gnac/%{name}-%{version}.tar.bz2
# Source0-md5:	14d86536a75bde9cbf4c5eaede8c4b2a
URL:		http://gnac.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gstreamer010-plugins-base-devel
BuildRequires:	gtk+3-devel
BuildRequires:	libunique3-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
Requires(post,post):	/usr/bin/gtk-update-icon-cache
Requires(post,post):	desktop-file-utils
Requires(post,post):	glib-gio-gsettings
Requires(post,post):	hicolor-icon-theme
Requires:	gstreamer010-plugins-bad
Requires:	gstreamer010-plugins-base
Requires:	gstreamer010-plugins-good
Requires:	gstreamer010-plugins-ugly
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnac is an easy to use audio conversion program for the Gnome desktop.
It is designed to be powerful but simple! It provides easy audio files
conversion between all GStreamer supported audio formats.

%prep
%setup -q

sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g'		\
    -i -e 's|AM_GST_ELEMENT_CHECK.*||g' configure.ac

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_iconsdir}/hicolor/256x256

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnac

%dir %{_datadir}/gnac
%{_datadir}/gnac/*.xml
%{_datadir}/gnac/profiles
%{_datadir}/glib-2.0/schemas/org.gnome.gnac.gschema.xml
%{_desktopdir}/gnac.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_mandir}/man1/gnac.1*

