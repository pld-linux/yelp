# TODO:
# move stylesheets to /usr/share/sgml
# use more generic stylesheet location
# remove docbook dtds and stylesheets from package and use system xml catalog
Summary:	A system documentation reader from the Gnome project
Summary(pl):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	1.0.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-pixmapsdir.patch
#Patch1:		%{name}-pld.patch
URL:		http://www.gnome.org/
Requires:	docbook-style-xsl = 1.50.0-1
Requires:	scrollkeeper
BuildRequires:	pkgconfig >= 0.12.0
BuildRequires:	ORBit2-devel >= 2.4.0
BuildRequires:	glib2-devel >= 2.0.3
BuildRequires:	libgtkhtml-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.0.1
BuildRequires:	libxslt-devel >= 1.0.15
BuildRequires:	GConf2-devel >= 1.2.0
BuildRequires:	bzip2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME2

%description
Yelp is the Gnome 2 help/documentation browser. It is designed to help
you browse all the documentation on your system in one central tool.

%description -l pl
Yelp jest przegl�dark� pomocy i dokumentacji GNOME 2. Ma pomaga� w
przegl�daniu ca�ej dokumentacji systemu w jednym, centralnym
narz�dziu.

%prep
%setup  -q 
%patch0 -p1
#%patch1 -p1

%build
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post 
GCONF_CONFIG_SOURCE="`%{_bindir}/gconftool-2 --get-default-source`" %{_bindir}/gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/*.schemas > /dev/null

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/applications/*
%{_libdir}/bonobo/servers/*
%attr(755,root,root) %{_libdir}/%{name}-db2html
%{_datadir}/sgml/docbook/%{name}
