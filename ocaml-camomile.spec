%define name	ocaml-camomile
%define version	0.7.1
%define release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Unicode library for OCaml
Group:      Development/Other
# Several files are MIT and UCD licensed, but the overall work is LGPLv2+
# and the LGPL/GPL supercedes compatible licenses.
# https://www.redhat.com/archives/fedora-legal-list/2008-March/msg00005.html
License:        LGPLv2+
URL:            http://sourceforge.net/projects/camomile/
Source0:        http://downloads.sourceforge.net/camomile/camomile-%{version}.tar.bz2
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Camomile is a Unicode library for ocaml. Camomile provides Unicode
character type, UTF-8, UTF-16, UTF-32 strings, conversion to/from
about 200 encodings, collation and locale-sensitive case mappings, and
more.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        data
Summary:        Data files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    data
The %{name}-data package contains data files for developing
applications that use %{name}.

%prep
%setup -q -n camomile-%{version}

%build
./configure --prefix=%{_prefix} --datadir=%{_datadir} --libdir=%{_libdir}
make
make dochtml
make man
strip tools/*.opt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_libdir}/ocaml
install -d -m 755 %{buildroot}%{_libdir}/ocaml/stublibs
install -d -m 755 %{buildroot}%{_bindir}
make install \
    prefix=%{buildroot}%{_prefix} \
    DATADIR=%{buildroot}%{_datadir} \
    DESTDIR=%{buildroot} \
    OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mv %{buildroot}%{_bindir}/camomilecharmap.opt \
    %{buildroot}%{_bindir}/camomilecharmap
mv %{buildroot}%{_bindir}/camomilelocaledef.opt \
    %{buildroot}%{_bindir}/camomilelocaledef

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%dir %{_libdir}/ocaml/camomile
%{_libdir}/ocaml/camomile/*.cmi
%{_libdir}/ocaml/camomile/*.cma
%{_libdir}/ocaml/camomile/META
%{_bindir}/camomilecharmap
%{_bindir}/camomilelocaledef

%files devel
%defattr(-,root,root)
%doc README dochtml/*
%{_libdir}/ocaml/camomile/*.a
%{_libdir}/ocaml/camomile/*.cmx
%{_libdir}/ocaml/camomile/*.cmxa
%{_libdir}/ocaml/camomile/*.mli

%files data
%defattr(-,root,root)
%doc README
%{_datadir}/camomile

