# TODO:
# move stylesheets to /usr/share/sgml
# use more generic stylesheet location
# remove docbook dtds and stylesheets from package and use system xml catalog
Summary:	A system documentation reader from the GNOME project
Summary(pl):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	2.6.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	9bd94af344ee6a0bf69aa6f9cbd6b7e9
Patch0:		%{name}-desktop-categories.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.6.1
BuildRequires:	ORBit2-devel >= 1:2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.6.1.1
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libgtkhtml-devel >= 2.6.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.9
BuildRequires:	libxslt-devel >= 1.1.5
BuildRequires:	pkgconfig >= 1:0.15.0
BuildRequires:	popt-devel
BuildRequires:	rpm-build >= 4.1-10
Requires(post):	GConf2
Requires:	docbook-style-xsl >= 1.55.0
Requires:	gnome-mime-data >= 2.4.1
Requires:	gnome-vfs2 >= 2.6.1.1
Requires:	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yelp is the GNOME 2 help/documentation browser. It is designed to help
you browse all the documentation on your system in one central tool.

%description -l pl
Yelp jest przegl�dark� pomocy i dokumentacji GNOME 2. Ma pomaga� w
przegl�daniu ca�ej dokumentacji systemu w jednym, centralnym
narz�dziu.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
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
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/bonobo/servers/*
%{_datadir}/sgml/docbook/%{name}
%{_desktopdir}/*
