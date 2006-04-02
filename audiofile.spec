Summary:	Audio File Library - SGI Audio File Library
Summary(es):	Biblioteca para manipulaci�n de varios archivos de sonido
Summary(pl):	Biblioteka Audio File - implementacja SGI Audio File Library
Summary(pt_BR):	Biblioteca para manipular v�rios formatos de arquivos de �udio
Summary(ru):	���������� ������ � ������� ��������� �����-������
Summary(uk):	��̦����� ������ � Ҧ����� ��������� ��Ħ�-���̦�
Name:		audiofile
Version:	0.2.6
Release:	3
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	3d01302834660850b6141cac1e6f5501
Patch0:		%{name}-am18.patch
Patch1:		%{name}-less_mem_hungry.patch
URL:		http://www.68k.org/~michael/audiofile/
BuildRequires:	automake
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
La Biblioteca de Archivos de Audio es una implementaci�n parcial de la
biblioteca de Archivos de Audio SGI. Dicha biblioteca permite el
procesado de datos de audio desde y para archivos de audio de los
formatos m�s comunes (actualmente AIFF, AIFC, WAVE, y NeXT/Sun).

Este software no est� completo y est� todav�a desarroll�ndose. Muchos
formatos de archivo de sonido funcionan correctamente. Otros no tanto.

%description -l pl
Biblioteka Audio File jest implementacj� biblioteki SGI Audio File.
Przy jej pomocy mo�na przetwarza� d�wi�ki w r�nych formatach (AIFF,
AIFC, WAVE i NeXT/Sun).

%description -l pt_BR
A biblioteca Audio File � uma implementa��o parcial da bibliotca Audio
File da SGI. Ela prov� processamento de dados de �udio de e para
v�rios formatos comuns (atualmente AIFF, AIFC, WAVE e NeXT/Sun).

Este software n�o est� completo e ainda est� em desenvolvimento.
Muitos formatos funcionam bem, outros ainda n�o.

%description -l ru
���������� ������ � ������� ��������� �����-������. ������������
������� esound.

%description -l uk
��̦����� ������ � Ҧ����� ��������� ��Ħ�-���̦�. ����������դ����
������� esound.

%package progs
Summary:	Audiofile programs
Summary(pl):	Programy audiofile
Summary(pt_BR):	Programas que acompanham a biblioteca audiofile
Group:		Applications/Sound

%description progs
audiofile applications.

%description progs -l pl
Programy audiofile.

%description progs -l pt_BR
Programas que acompanham a audiofile.

%package devel
Summary:	Header and other files to develop Audio File applications
Summary(es):	Archivos de inclusi�n y otros archivos para el desarrollo de aplicaciones audiofile
Summary(pl):	Pliki nag��wkowe i inne potrzebe do Audio File
Summary(pt_BR):	Arquivos de inclus�o e outros arquivos para desenvolver aplicativos audiofile
Summary(ru):	����� ��� ���������� ���������� � �������������� audiofile
Summary(uk):	����� ��� �������� ���������� ������� � ������������� audiofile
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libaudiofile-devel
Obsoletes:	libaudiofile0-devel

%description devel
Header and other files to develop Audio File applications.

%description devel -l pl
Pliki nag��wkowe biblioteki Audio File, czyli to, co jest potrzebne do
tworzenia aplikacji korzystaj�cych z tej biblioteki.

%description devel -l es
Archivos de inclusi�n y otros archivos para el desarrollo de
aplicaciones audiofile.

%description devel -l pt_BR
Arquivos de inclus�o e outros arquivos para desenvolver aplicativos
audiofile.

%description devel -l ru
.h-����� � ��. ��� ���������� ���������� � �������������� audiofile.

%description devel -l uk
.h-����� �� ���� ��� �������� ���������� ������� � �������������
audiofile.

%package static
Summary:	Static libaudiofile libraries
Summary(pl):	Biblioteka statyczne libaudiofile
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com audiofile
Summary(ru):	����������� ���������� ��� ���������� ���������� � �������������� audiofile
Summary(uk):	������Φ ¦�̦����� ��� �������� ���������� ������� � ������������� audiofile
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libaudiofile-static

%description static
Static libaudiofile libraries.

%description static -l pl
Biblioteki statyczne libaudiofile.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com audiofile

%description static -l ru
����������� ���������� ��� ���������� ���������� � ��������������
audiofile.

%description static -l uk
������Φ ¦�̦����� ��� �������� ���������� ������� � �������������
audiofile.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp /usr/share/automake/config.sub .
%configure \
	--enable-largefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
