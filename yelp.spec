#
# Conditinal build:
%bcond_without	mozilla_firefox		# build with mozilla-firefox
#
Summary:	A system documentation reader from the GNOME project
Summary(pl):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	2.14.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/yelp/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	4294fe3b01824675bd8be9d7936dcaa7
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-m4.patch
Patch2:		%{name}-bs.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	ORBit2-devel >= 1:2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.4.0
BuildRequires:	gnome-vfs2-devel >= 2.14.2
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.14.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.21
BuildRequires:	libxslt-devel >= 1.1.5
%if %{with mozilla_firefox}
BuildRequires:	mozilla-firefox-devel
%else
BuildRequires:	mozilla-devel >= 5:1.7
%endif
BuildRequires:	pkgconfig >= 1:0.15.0
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	zlib-devel
Requires(post,preun):	GConf2
Requires:	docbook-style-xsl >= 1.55.0
Requires:	gnome-doc-utils >= 0.4.0
Requires:	gnome-vfs2 >= 2.14.2
Requires:	libgnomeui >= 2.14.1
Requires:	scrollkeeper
%if %{with mozilla_firefox}
%requires_eq	mozilla-firefox
%else
Requires:	mozilla-embedded = %(rpm -q --qf '%{EPOCH}:%{VERSION}' --whatprovides mozilla-embedded)
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# can be provided by mozilla or mozilla-embedded
%define		_noautoreqdep	libgtkembedmoz.so libgtksuperwin.so libxpcom.so

%description
Yelp is the GNOME help/documentation browser. It is designed to help
you browse all the documentation on your system in one central tool.

%description -l pl
Yelp jest przegl±dark± pomocy i dokumentacji GNOME. Umo¿liwia
przegl±danie ca³ej dokumentacji systemu za pomoc± jednego, centralnego
narzêdzia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install yelp.schemas

%preun
%gconf_schema_uninstall yelp.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_iconsdir}/hicolor/192x192/apps/yelp-icon-big.png
%{_sysconfdir}/gconf/schemas/yelp.schemas
