
%define		snap	20021108

Summary:	Audio File Library - SGI Audio File Library
Summary(es):	Biblioteca para manipulaciСn de varios archivos de sonido
Summary(pl):	Biblioteka Audio File - implementacja SGI Audio File Library
Summary(pt_BR):	Biblioteca para manipular vАrios formatos de arquivos de Аudio
Summary(ru):	Библиотека работы с разными форматами аудио-файлов
Summary(uk):	Б╕бл╕отека роботи з р╕зними форматами ауд╕о-файл╕в
Name:		audiofile
Version:	0.2.3
Release:	5.%{snap}.1
Epoch:		1
License:	LGPL
Group:		Libraries
#Source0:	ftp://oss.sgi.com/projects/audiofile/download/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.%{snap}.tar.bz2
# Source0-md5: eb83db508061a9d6c22984de3d4be5d3
URL:		http://oss.sgi.com/projects/audiofile/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libaudiofile
Obsoletes:	libaudiofile0

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

%description -l es
La Biblioteca de Archivos de Audio es una implementaciСn parcial de la
biblioteca de Archivos de Audio SGI. Dicha biblioteca permite el
procesado de datos de audio desde y para archivos de audio de los
formatos mАs comunes (actualmente AIFF, AIFC, WAVE, y NeXT/Sun).

Este software no estА completo y estА todavМa desarrollАndose. Muchos
formatos de archivo de sonido funcionan correctamente. Otros no tanto.

%description -l pl
Biblioteka Audio File jest implementacj╠ biblioteki SGI Audio File.
Przy jej pomocy mo©na przetwarzaФ d╪wiЙki w rС©nych formatach (AIFF,
AIFC, WAVE i NeXT/Sun).

%description -l pt_BR
A biblioteca Audio File И uma implementaГЦo parcial da bibliotca Audio
File da SGI. Ela provЙ processamento de dados de Аudio de e para
vАrios formatos comuns (atualmente AIFF, AIFC, WAVE e NeXT/Sun).

Este software nЦo estА completo e ainda estА em desenvolvimento.
Muitos formatos funcionam bem, outros ainda nЦo.

%description -l ru
Библиотека работы с разными форматами фудио-файлов. Используется
демоном esound.

%description -l uk
Б╕бл╕отека роботи з р╕зними форматами ауд╕о-файл╕в. Використову╓ться
демоном esound.

%package progs
Summary:	Audiofile programs
Summary(es):	Audiofile programs
Summary(pl):	Programy audiofile
Summary(pt_BR):	Programas que acompanham a biblioteca audiofile
Group:		Applications/Sound

%description progs
audiofile applications.

%description progs -l es
Audiofile programs.

%description progs -l pl
Programy audiofile.

%description progs -l pt_BR
Programas que acompanham a audiofile.

%package devel
Summary:	Header files and others to develop Audio File applications
Summary(es):	Bibliotecas, archivos de inclusiСn y otros archivos para el desarrollo de aplicaciones audiofile
Summary(pl):	Pliki nagЁСwkowe i inne potrzebe do Audio File
Summary(pt_BR):	Bibliotecas, arquivos de inclusЦo e outros arquivos para desenvolver aplicativos audiofile
Summary(ru):	Файлы для разработки приложений с использованием audiofile
Summary(uk):	Файли для розробки прикладних програм з використанням audiofile
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Obsoletes:	libaudiofile-devel
Obsoletes:	libaudiofile0-devel

%description devel
Header files and others to develop Audio File applications.

%description devel -l pl
Pliki nagЁСwkСw do Audio File'a, czyli to czego potrzebujesz do
tworzenia aplikacji pod Audio File'm.

%description devel -l es
Bibliotecas, archivos de inclusiСn y otros archivos para el desarrollo
de aplicaciones audiofile.

%description devel -l pt_BR
Bibliotecas, arquivos de inclusЦo e outros arquivos para desenvolver
aplicativos audiofile.

%description devel -l ru
.h-файлы и пр. для разработки приложений с использованием audiofile.

%description devel -l uk
.h-файли та ╕нше для розробки прикладних програм з використанням
audiofile.

%package static
Summary:	Static libaudiofile libraries
Summary(es):	Static libraries for audiofile development
Summary(pl):	Biblioteka statyczne libaudiofile
Summary(pt_BR):	Bibliotecas estАticas para desenvolvimento com audiofile
Summary(ru):	Статические библиотеки для разработки приложений с использованием audiofile
Summary(uk):	Статичн╕ б╕бл╕отеки для розробки прикладних програм з використанням audiofile
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}
Obsoletes:	libaudiofile-static

%description static
Static libaudiofile libraries.

%description static -l es
Static libraries for audiofile development

%description static -l pl
Biblioteki statyczne libaudiofile.

%description static -l pt_BR
Bibliotecas estАticas para desenvolvimento com audiofile

%description static -l ru
Статические библиотеки для разработки приложений с использованием
audiofile.

%description static -l uk
Статичн╕ б╕бл╕отеки для розробки прикладних програм з використанням
audiofile.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir} \
	pkgconfig=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NOTES README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sfconvert
%attr(755,root,root) %{_bindir}/sfinfo

%files devel
%defattr(644,root,root,755)

%attr(755,root,root) %{_bindir}/audiofile-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la

%{_includedir}/*
%{_aclocaldir}/audiofile.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
