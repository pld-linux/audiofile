Summary:	Audio File Library - SGI Audio File Library
Summary(pl):	Biblioteka Audio File - implementacja SGI Audio File Library
Name:		audiofile
Version:	0.1.11
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Source0:	ftp://ftp.68k.org./pub/michael/%{name}-%{version}.tar.gz
Patch0:		%{name}-automake_fix.patch
URL:		http://www.68k.org/~michael/audiofile/
BUildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libaudiofile

%description
This Audio File Library is an implementation of the SGI Audio File
library. Since the latter is specified ambiguously in places, I've
taken some liberties in interpreting certain such ambiguities. At the
present, not all features of the SGI Audio File library are
implemented. I feel, though, that this implementation of the Audio
File Library offers enough functionality to be useful for general
tasks. This library allows the processing of audio data to and from
audio files of many common formats (currently AIFF, AIFC, WAVE, and
NeXT/Sun).

%description -l pl
Biblioteka Audio File jest implementacj� biblioteki SGI Audio File.
Przy jej pomocy mo�na przetwarza� d�wi�ki w r�nych formatach (AIFF,
AIFC, WAVE i NeXT/Sun).

%package devel
Summary:	Header files and others to develop Audio File applications
Summary(pl):	Pliki nag��wkowe i inne potrzebe do Audio File
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Obsoletes:	libaudiofile-devel

%description devel
Header files and others to develop Audio File applications.

%description -l pl devel
Pliki nag��wk�w do Audio File'a, czyli to czego potrzebujesz do
tworzenia aplikacji pod Audio File'm.

%package static
Summary:	Static libaudiofile libraries
Summary(pl):	Biblioteka statyczne libaudiofile
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}
Obsoletes:	libaudiofile-static

%description static
Static libaudiofile libraries.

%description -l pl static
Biblioteki statyczne libaudiofile.

%prep
%setup -q
%patch -p1

%build
automake
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

gzip -9nf NOTES README TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NOTES,README,TODO}.gz

%attr(755,root,root) %{_bindir}/sfconvert
%attr(755,root,root) %{_bindir}/sfinfo
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/audiofile-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la

%{_includedir}/*
%{_aclocaldir}/audiofile.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
