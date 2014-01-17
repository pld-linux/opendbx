#
# Conditional build:
%bcond_without	ibase		# don't build ibase (InterBase/Firebird) backend

%ifnarch %{ix86} %{x8664} sparc sparcv9 alpha ppc
%undefine	with_ibase
%endif

Summary:	Extensible library for database access
Summary(pl.UTF-8):	Rozszerzana biblioteka dostępu do baz danych
Name:		opendbx
Version:	1.4.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://linuxnetworks.de/opendbx/download/%{name}-%{version}.tar.gz
# Source0-md5:	3e89d7812ce4a28046bd60d5f969263d
URL:		http://www.linuxnetworks.de/doc/index.php/OpenDBX
%{?with_ibase:BuildRequires:	Firebird-devel}
BuildRequires:	freetds-devel
BuildRequires:	mysql-devel
BuildRequires:	postgresql-devel
BuildRequires:	sqlite-devel
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		skip_post_check_so	libmssqlbackend.so.1.2.0

%description
OpenDBX is an extremely lightweight but extensible database access
library written in C. It provides an abstraction layer to all
supported databases with a single, clean and simple interface that
leads to an elegant code design automatically. If you want your
application to support different databases with little effort, this is
definitively the right thing for you!

%description -l pl.UTF-8
OpenDBX to skrajnie lekka, ale rozszerzalna biblioteka dostępu do baz
danych napisana w C. Udostępnia warstwę abstrakcji dla wszystkich
obsługiwanych baz danych w jednym, przejrzystym i prostym interfejsie
automatycznie prowadzącym do eleganckiego projektu kodu. Jest to
odpowiednia biblioteka, aby małym nakładem pracy aplikacja obsługiwała
różne bazy danych.

%package devel
Summary:	Header files for opendbx
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki opendbx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for opendbx.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki opendbx.

%package static
Summary:	Static opendbx library
Summary(pl.UTF-8):	Statyczna biblioteka opendbx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static opendbx library.

%description static -l pl.UTF-8
Statyczna biblioteka opendbx.

%package backend-firebird
Summary:	Firebird backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych Firebird dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-firebird
Firebird backend for opendbx.

%description backend-firebird -l pl.UTF-8
Backend bazy danych Firebird dla biblioteki opendbx.

%package backend-mssql
Summary:	MS SQL backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych MS SQL dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-mssql
MS SQL backend for opendbx.

%description backend-mssql -l pl.UTF-8
Backend bazy danych MS SQL dla biblioteki opendbx.

%package backend-mysql
Summary:	MySQL backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych MySQL dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-mysql
MySQL backend for opendbx.

%description backend-mysql -l pl.UTF-8
Backend bazy danych MySQL dla biblioteki opendbx.

%package backend-postgres
Summary:	PostgreSQL backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych PostgreSQL dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-postgres
PostgreSQL backend for opendbx.

%description backend-postgres -l pl.UTF-8
Backend bazy danych PostgreSQL dla biblioteki opendbx.

%package backend-sqlite3
Summary:	sqlite3 backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych sqlite3 dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-sqlite3
sqlite3 backend for opendbx.

%description backend-sqlite3 -l pl.UTF-8
Backend bazy danych sqlite3 dla biblioteki opendbx.

%package backend-sqlite
Summary:	sqlite backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych sqlite dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-sqlite
sqlite backend for opendbx.

%description backend-sqlite -l pl.UTF-8
Backend bazy danych sqlite dla biblioteki opendbx.

%package backend-sybase
Summary:	sybase backend for opendbx
Summary(pl.UTF-8):	Backend bazy danych sybase dla biblioteki opendbx
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description backend-sybase
sybase backend for opendbx.

%description backend-sybase -l pl.UTF-8
Backend bazy danych sybase dla biblioteki opendbx.

%prep
%setup -q

%build
CPPFLAGS="-I/usr/include/mysql"; export CPPFLAGS
%configure \
	--with-backends="%{?with_ibase:firebird} mssql mysql pgsql sqlite sqlite3 sybase"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post backend-firebird
/sbin/ldconfig -n %{_libdir}/%{name}

%postun backend-firebird
/sbin/ldconfig -n %{_libdir}/%{name}

%post backend-mssql
/sbin/ldconfig -n %{_libdir}/%{name}

%postun backend-mssql
/sbin/ldconfig -n %{_libdir}/%{name}

%post backend-mysql
/sbin/ldconfig -n %{_libdir}/%{name}

%postun backend-mysql
/sbin/ldconfig -n %{_libdir}/%{name}

%post backend-postgres
/sbin/ldconfig -n %{_libdir}/%{name}

%postun backend-postgres
/sbin/ldconfig -n %{_libdir}/%{name}

%post backend-sqlite3
/sbin/ldconfig -n %{_libdir}/%{name}

%postun backend-sqlite
/sbin/ldconfig -n %{_libdir}/%{name}

%post backend-sybase
/sbin/ldconfig -n %{_libdir}/%{name}

%postun backend-sybase
/sbin/ldconfig -n %{_libdir}/%{name}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/* AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/odbx-sql
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.1
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/keywords
%dir %{_libdir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/opendbx
%{_includedir}/*.h
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%if %{with ibase}
%files backend-firebird
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libfirebird*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}/libfirebird*.so.1
%attr(755,root,root) %{_libdir}/%{name}/libfirebird*.so
%{_libdir}/%{name}/libfirebird*.la
%endif

%files backend-mssql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libmssql*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}/libmssql*.so.1
%attr(755,root,root) %{_libdir}/%{name}/libmssql*.so
%{_libdir}/%{name}/libmssql*.la

%files backend-mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libmysql*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}/libmysql*.so.1
%attr(755,root,root) %{_libdir}/%{name}/libmysql*.so
%{_libdir}/%{name}/libmysql*.la

%files backend-postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libpgsql*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}/libpgsql*.so.1
%attr(755,root,root) %{_libdir}/%{name}/libpgsql*.so
%{_libdir}/%{name}/libpgsql*.la

%files backend-sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libsqlite3*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}/libsqlite3*.so.1
%attr(755,root,root) %{_libdir}/%{name}/libsqlite3*.so
%{_libdir}/%{name}/libsqlite3*.la

%files backend-sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libsqliteb*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}/libsqliteb*.so.1
%attr(755,root,root) %{_libdir}/%{name}/libsqliteb*.so
%{_libdir}/%{name}/libsqliteb*.la

%files backend-sybase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libsybase*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}/libsybase*.so.1
%attr(755,root,root) %{_libdir}/%{name}/libsybase*.so
%{_libdir}/%{name}/libsybase*.la
