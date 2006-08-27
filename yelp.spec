Summary:	A system documentation reader from the GNOME project
Summary(pl):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	2.15.91
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/yelp/2.15/%{name}-%{version}.tar.bz2
# Source0-md5:	4e80d89cf67360f7f2496cf87d0c83c4
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-bs.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	ORBit2-devel >= 1:2.14.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	beagle-devel >= 0.2.7
BuildRequires:	bzip2-devel
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gnome-doc-utils >= 0.7.2
BuildRequires:	gnome-vfs2-devel >= 2.15.91
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	libxslt-devel >= 1.1.17
BuildRequires:	mozilla-firefox-devel >= 1.5.0.6
BuildRequires:	pkgconfig >= 1:0.15.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	zlib-devel
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	gtk+2 >= 2:2.10.1
Requires:	docbook-style-xsl >= 1.55.0
Requires:	gnome-doc-utils >= 0.7.2
Requires:	gnome-vfs2 >= 2.15.91
Requires:	libgnomeui >= 2.15.91
Requires:	scrollkeeper
%requires_eq	mozilla-firefox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# can be provided by mozilla or mozilla-embedded
%define		_noautoreqdep	libgtkembedmoz.so libgtksuperwin.so libxpcom.so

%description
Yelp is the GNOME help/documentation browser. It is designed to help
you browse all the documentation on your system in one central tool.

%description -l pl
Yelp jest przegl�dark� pomocy i dokumentacji GNOME. Umo�liwia
przegl�danie ca�ej dokumentacji systemu za pomoc� jednego, centralnego
narz�dzia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ug

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install yelp.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall yelp.schemas

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_iconsdir}/hicolor/*/*/yelp-icon-big.png
%{_sysconfdir}/gconf/schemas/yelp.schemas
