# TODO:
# move stylesheets to /usr/share/sgml
# use more generic stylesheet location
# remove docbook dtds and stylesheets from package and use system xml catalog
Summary:	A system documentation reader from the Gnome project
Summary(pl):	Czytnik dokumentacji z projektu GNOME
Name:		yelp
Version:	2.1.2
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
Patch0:		%{name}-pixmapsdir.patch
#Patch1:		%{name}-pld.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 1.2.1
BuildRequires:	ORBit2-devel >= 2.4.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	gnome-vfs2-devel >= 2.0.4-3
BuildRequires:	libgnome-devel >= 2.0.4
BuildRequires:	libgnomeui-devel >= 2.0.5
BuildRequires:	libgtkhtml-devel >= 2.1.2
BuildRequires:	libxslt-devel >= 1.0.20
BuildRequires:	pkgconfig >= 0.12.0
BuildRequires:	rpm-build >= 4.1-7
Requires(post):	GConf2
Requires:	docbook-style-xsl >= 1.55.0
Requires:	scrollkeeper
Requires:	gnome-vfs2 >= 2.0.4-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11/GNOME2
%define		_serverdir	/usr/lib/bonobo/servers

%description
Yelp is the Gnome 2 help/documentation browser. It is designed to help
you browse all the documentation on your system in one central tool.

%description -l pl
Yelp jest przegl±dark± pomocy i dokumentacji GNOME 2. Ma pomagaæ w
przegl±daniu ca³ej dokumentacji systemu w jednym, centralnym
narzêdziu.

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

%{__make} install \
	    DESTDIR=$RPM_BUILD_ROOT \
	    serverdir=%{_serverdir}

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
%{_datadir}/pixmaps/%{name}
%{_datadir}/applications/*
%{_serverdir}/*
%attr(755,root,root) %{_libdir}/%{name}-db2html
%{_datadir}/sgml/docbook/%{name}
