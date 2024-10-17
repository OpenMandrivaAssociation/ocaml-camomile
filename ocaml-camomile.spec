%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Unicode library for OCaml
Name:		ocaml-camomile
Version:	0.8.4
Release:	2
# Several files are MIT and UCD licensed, but the overall work is LGPLv2+
# and the LGPL/GPL supercedes compatible licenses.
# https://www.redhat.com/archives/fedora-legal-list/2008-March/msg00005.html
License:	LGPLv2+
Group:		Development/Other
Url:		https://sourceforge.net/projects/camomile/
Source0:	http://downloads.sourceforge.net/camomile/camomile-%{version}.tar.bz2
Source10:	%{name}.rpmlintrc
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
Camomile is a Unicode library for ocaml. Camomile provides Unicode
character type, UTF-8, UTF-16, UTF-32 strings, conversion to/from
about 200 encodings, collation and locale-sensitive case mappings, and
more.

%files
%doc README
%dir %{_libdir}/ocaml/camomile
%{_libdir}/ocaml/camomile/*.cmi
%{_libdir}/ocaml/camomile/*.cma
%{_libdir}/ocaml/camomile/META
%{_bindir}/camomile*
%{_bindir}/parse_*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc README dochtml/*
%{_libdir}/ocaml/camomile/*.a
%{_libdir}/ocaml/camomile/*.cmx
%{_libdir}/ocaml/camomile/*.cmxa
%{_libdir}/ocaml/camomile/*.mli

#----------------------------------------------------------------------------

%package data
Summary:	Data files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description data
The %{name}-data package contains data files for developing
applications that use %{name}.

%files data
%doc README
%{_datadir}/camomile

#----------------------------------------------------------------------------

%prep
%setup -q -n camomile-%{version}

%build
./configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir} \
	--libdir=%{_libdir}
make
make dochtml
make man
strip tools/*.opt

%install
install -d -m 755 %{buildroot}%{_libdir}/ocaml
install -d -m 755 %{buildroot}%{_libdir}/ocaml/stublibs
install -d -m 755 %{buildroot}%{_bindir}
make install \
	prefix=%{buildroot}%{_prefix} \
	DATADIR=%{buildroot}%{_datadir} \
	DESTDIR=%{buildroot} \
	OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml

pushd tools
for f in *.opt ; do  install -m 0755 $f %{buildroot}%{_bindir}/${f%.opt} ; done
popd

