%define gtk2_version 1.3.13
%define gtkhtml2_version 1.99.2
%define gnome_vfs2_version 1.9.4.91
%define libgnomeui_version 1.110.0
%define libbonobo_version 1.110.0

Summary: A system documentation reader from the Gnome project. 
Name: yelp
Version: 0.2
Release: 2
Source0: yelp-0.2.tar.bz2
License: GPL
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-root
Requires: scrollkeeper
Requires: gtk2 >= %{gtk2_version}
Requires: gnome-vfs2 >= %{gnome_vfs2_version}
Requires: gtkhtml2 >= %{gtkhtml2_version}
Requires: libgnomeui >= %{libgnomeui_version}
Requires: libbonobo >= %{libbonobo_version}
BuildRequires: gtk2-devel >= %{gtk2_version}
BuildRequires: gnome-vfs2-devel >= %{gnome_vfs2_version}
BuildRequires: gtkhtml2-devel >= %{gtkhtml2_version}
BuildRequires: libgnomeui-devel >= %{libgnomeui_version}
BuildRequires: libbonobo-devel >= %{libbonobo_version}

%description
Yelp is the Gnome 2 help/documentation browser. It is designed
to help you browse all the documentation on your system in
one central tool.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/yelp
%{_libdir}/bonobo/servers/GNOME_Yelp.server
%{_datadir}/applications/yelp.desktop
%{_datadir}/yelp

%changelog
* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Rebuild for new gnome2 libraries

* Mon Jan 28 2002 Alex Larsson <alexl@redhat.com>
- Initial build.
