# TODO:
#	- what is that huge %post script?
#
# Conditional build:
%bcond_without	apidocs			# documentation generated with doxygen
%bcond_without	java			# Java bindings
%bcond_without	ocaml			# OCaml bindings
%bcond_without	python			# Python bindings
%bcond_without	python3			# Python 3.x bindings
%bcond_without	tcl			# Tcl bindings
%bcond_without	x			# X11-based utilities
%bcond_without	gpm			# mouse tracking via GPM
%bcond_without	libbraille		# libbraille Braille driver
%bcond_without	liblouis		# liblouis in-line contracted Braille support
%bcond_without	espeak			# eSpeak synthesizer driver
%bcond_without	espeak_ng		# eSpeak-NG synthesizer driver
%bcond_without	flite			# Flite synthesizer driver
%bcond_with	mikropuhe		# Mikropuhe synthesizer driver [commercial, Finnish]
%bcond_without	speech_dispatcher	# Speech Dispatcher synthesizer driver
%bcond_with	swift			# Swift synthesizer driver [commercial, from Cepstral]
%bcond_with	theta			# Theta synthesizer driver [commercial, from Cepstral]
%bcond_with	viavoice		# IBM ViaVoice synthesizer driver [commercial]
%bcond_with	at_spi			# AtSpi screen driver
%bcond_without	at_spi2			# AtSpi2 screen driver

%define		brlapi_ver	0.7.0
%include	/usr/lib/rpm/macros.java
Summary:	Braille display driver for Linux/Unix
Summary(pl.UTF-8):	Sterownik do wyświetlaczy Braille'a
Name:		brltty
Version:	6.0
Release:	1
License:	GPL v2+ (brltty and drivers), LGPL v2.1+ (APIs)
Group:		Daemons
Source0:	http://mielke.cc/brltty/archive/%{name}-%{version}.tar.xz
# Source0-md5:	feca8c2f22b13a4c67b1366191033c0e
Patch1:		%{name}-speech-dispatcher.patch
Patch2:		%{name}-python.patch
Patch3:		make.patch
Patch4:		%{name}-glibc25.patch
URL:		http://mielke.cc/brltty/
BuildRequires:	alsa-lib-devel
%{?with_at_spi:BuildRequires:	at-spi-devel}
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	bison
# just headers
BuildRequires:	bluez-libs-devel
%{?with_at_spi2:BuildRequires:	dbus-devel >= 1.0}
%{?with_apidocs:BuildRequires:	doxygen}
%{?with_espeak:BuildRequires:	espeak-devel}
%{?with_espeak_ng:BuildRequires:	espeak-ng-devel}
BuildRequires:	expat-devel
%{?with_flite:BuildRequires:	flite-devel}
BuildRequires:	gettext-tools
%{?with_gpm:BuildRequires:	gpm-devel}
%{?with_java:BuildRequires:	jdk}
%{?with_java:BuildRequires:	jpackage-utils}
%{?with_libbraille:BuildRequires:	libbraille-devel}
BuildRequires:	libicu-devel
%{?with_liblouis:BuildRequires:	liblouis-devel}
BuildRequires:	ncurses-devel
%{?with_ocaml:BuildRequires:	ocaml}
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
%{?with_python:BuildRequires:	python-Cython}
%{?with_python3:BuildRequires:	python3-Cython}
%{?with_java:BuildRequires:	rpm-javaprov}
%{?with_python:BuildRequires:	rpm-pythonprov}
BuildRequires:	rpmbuild(macros) >= 1.710
%{?with_speech_dispatcher:BuildRequires:	speech-dispatcher-devel >= 0.8}
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
%{?with_tcl:BuildRequires:	tcl-devel >= 8.5}
%if %{with x}
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
%endif
#%{?with_mikropuhe:BuildRequires:	Mikropuhe-devel (-lmikropuhe <mpwrfile.h>)}
#%{?with_swift:BuildRequires:	Swift-devel (-lswift <swift.h>)}
#%{?with_theta:BuildRequires:	Theta-devel (-ltheta <theta.h>)}
#%{?with_viavoice:BuildRequires:	ViaVoice-devel (-libmeci50 <eci.h>)}
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BRLTTY is a background process (daemon) which provides access to the
Linux/Unix console (when in text mode) for a blind person using a
refreshable Braille display. It drives the Braille display, and
provides complete screen review functionality. Some speech capability
has also been incorporated.

%description -l pl.UTF-8
BRLTTY jest demonem, który udostępnia dostęp do linuksowej konsoli (w
trybie tekstowym) dla niewidomych używających wyświetlaczy Braille'a z
odświeżaniem (refreshable Braille display). BRLTTY steruje
wyświetlaczem Braille'a i dostarcza funkcjonalność całkowitego
przeglądu ekranu. Do tego pakietu została włączona możliwość syntezy
mowy.

%package -n brlapi
Summary:	Application Programming Interface for BRLTTY
Summary(pl.UTF-8):	API do BRLTTY
License:	LGPL v2.1+
Group:		Libraries

%description -n brlapi
This package provides the run-time support for the Application
Programming Interface to BRLTTY.

Install this package if you have an application which directly
accesses a refreshable Braille display.

%description -n brlapi -l pl.UTF-8
Ten pakiet zawiera środowisko uruchomieniowe dla programów
korzystających z API BRLTTY.

Zainstaluj ten pakiet jeśli masz aplikację, która bezpośrednio używa
wyświetlacza Braille'a z odświeżaniem.

%package -n brlapi-devel
Summary:	Headers and documentation for BrlAPI
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do BrlAPI
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	brlapi = %{version}-%{release}

%description -n brlapi-devel
This package provides the header files, shared object linker
reference, and reference documentation for BrlAPI (the Application
Programming Interface to BRLTTY). It enables the implementation of
applications which take direct advantage of a refreshable Braille
display in order to present information in ways which are more
appropriate for blind users and/or to provide user interfaces which
are more specifically atuned to their needs.

Install this package if you're developing or maintaining an
application which directly accesses a refreshable Braille display.

%description -n brlapi-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe oraz dokumentację do BrlAPI (API
do BRLTTY). BrlAPI pozwala implementować aplikacje, które bezpośrednio
korzystają z wyświetlaczy Braille'a dostarczając interfejs użytkownika
bardziej przystosowany dla osób niewidomych.

Zainstaluj ten pakiet, jeśli tworzysz lub nadzorujesz aplikację
korzystającą bezpośrednio z odświeżalnych wyświetlaczy Braille'a.

%package -n brlapi-static
Summary:	Static BrlAPI library
Summary(pl.UTF-8):	Statyczna biblioteka BrlAPI
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	brlapi-devel = %{version}-%{release}

%description -n brlapi-static
This is package with static BrlAPI library.

%description -n brlapi-static -l pl.UTF-8
Ten pakiet zawiera statyczną wersję biblioteki BrlAPI.

%package -n brlapi-apidocs
Summary:	BrlAPI documentation
Summary(pl.UTF-8):	Documentacja BrlAPI
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n brlapi-apidocs
Documentation for BrlAPI in HTML format generated from brltty sources
by doxygen.

%description -n brlapi-apidocs -l pl.UTF-8
Dokumentacja BrlAPI w formacie HTML generowane ze źrodeł brltty przez
doxygen.

%package -n java-brlapi
Summary:	BrlAPI library for Java
Summary(pl.UTF-8):	Biblioteka BrlAPI dla Javy
License:	LGPL v2.1+
Group:		Libraries
Requires:	brlapi = %{version}-%{release}

%description -n java-brlapi
BrlAPI library for Java.

%description -n java-brlapi -l pl.UTF-8
Biblioteka BrlAPI dla Javy.

%package -n ocaml-brlapi
Summary:	OCaml binding for BrlAPI
Summary(pl.UTF-8):	Wiązania OCamla do BrlAPI
License:	LGPL v2.1+
Group:		Libraries
Requires:	brlapi = %{version}-%{release}
%requires_eq	ocaml-runtime

%description -n ocaml-brlapi
OCaml binding for BrlAPI.

%description -n ocaml-brlapi -l pl.UTF-8
Wiązania OCamla do BrlAPI.

%package -n ocaml-brlapi-devel
Summary:	OCaml binding for BrlAPI - development files
Summary(pl.UTF-8):	Wiązania OCamla do BrlAPI - pliki programistyczne
License:	LGPL v2.1+
Group:		Libraries
Requires:	ocaml-brlapi = %{version}-%{release}
%requires_eq	ocaml

%description -n ocaml-brlapi-devel
OCaml binding for BrlAPI - development files.

%description -n ocaml-brlapi-devel -l pl.UTF-8
Wiązania OCamla do BrlAPI - pliki programistyczne.

%package -n python-brlapi
Summary:	Python 2.x interface to BrlAPI
Summary(pl.UTF-8):	Interfejs Pythona 2.x do BrlAPI
License:	LGPL v2.1+
Group:		Libraries
Requires:	brlapi = %{version}-%{release}

%description -n python-brlapi
Python 2.x interface to BrlAPI.

%description -n python-brlapi -l pl.UTF-8
Interfejs Pythona 2.x do BrlAPI.

%package -n python3-brlapi
Summary:	Python 3.x interface to BrlAPI
Summary(pl.UTF-8):	Interfejs Pythona 3.x do BrlAPI
License:	LGPL v2.1+
Group:		Libraries
Requires:	brlapi = %{version}-%{release}

%description -n python3-brlapi
Python 3.x interface to BrlAPI.

%description -n python3-brlapi -l pl.UTF-8
Interfejs Pythona 3.x do BrlAPI.

%package -n brlapi-tcl
Summary:	BrlAPI library for Tcl
Summary(pl.UTF-8):	Biblioteka BrlAPI dla Tcl
License:	LGPL v2.1+
Group:		Libraries
Requires:	brlapi = %{version}-%{release}

%description -n brlapi-tcl
BrlAPI library for Tcl.

%description -n brlapi-tcl -l pl.UTF-8
Biblioteka BrlAPI dla Tcl.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
#patch3 -p1
%patch4 -p1

%build
%{__autoconf}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	%{?with_java:JAVA_HOME=%{java_home}} \
	--with-install-root="$RPM_BUILD_ROOT" \
	%{!?with_libbraille:--without-libbraille} \
	%{!?with_espeak:--without-espeak} \
	%{!?with_espeak_ng:--without-espeak_ng} \
	%{!?with_flite:--without-flite} \
	%{!?with_speech_dispatcher:--without-speechd} \
	%{!?with_ocaml:--disable-caml-bindings} \
	%{!?with_gpm:--disable-gpm} \
	%{!?with_java:--disable-java-bindings} \
	%{!?with_liblouis:--disable-liblouis} \
	--enable-lisp-bindings \
	%{!?with_python:--disable-python-bindings} \
	%{!?with_tcl:--disable-tcl-bindings} \
	%{!?with_x:--disable-x} \
	--enable-api

%{__make} -j1

%if %{with python}
cd Bindings/Python
%py_build
cd ../..
%endif

%if %{with python3}
cd Bindings/Python
%py3_build
cd ../..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install install-appstream \
	OCAML_INSTALL_TARGET=install-without-findlib

# findlib-specific, useless in rpm
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/dllbrlapi_stubs.so.owner

%if %{with python}
cd Bindings/Python
%py_install
cd ../..
%endif

%if %{with python3}
cd Bindings/Python
%py3_install
cd ../..
%endif

%if %{_lib} != "lib"
	# Fix java plugin install path on 64-bit archs
	install -d $RPM_BUILD_ROOT%{_libdir}/java
	%{__mv} $RPM_BUILD_ROOT%{_prefix}/{lib,%{_lib}}/java/libbrlapi_java.so
%endif

cp -p Documents/brltty.conf $RPM_BUILD_ROOT%{_sysconfdir}

install -d $RPM_BUILD_ROOT%{systemdtmpfilesdir}
cat >$RPM_BUILD_ROOT%{systemdtmpfilesdir}/brltty.conf <<EOF
d /var/run/brltty 0755 root root -
EOF

# no sign in source wheter it is zh_CN or zh_TW
# but seems to contain Traditional Chinese characters
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{zh,zh_TW}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# The pre-install scriptlet.

# If a configuration file already exists then rpm installs the new one as
# <path>.rpmnew. If this is done then the .rpmnew file is overwritten if it
# already exists.

# There's no explicit way to tell if a configuration file has been installed
# as itself or as a .rpmnew file. The way we'll figure it out, therefore, is by
# erasing the .rpmnew file now so that we can see if it gets created later.
rm -f "%{_sysconfdir}/brltty.conf.rpmnew"

%post
# The post-install scriptlet.

# If BRLTTY's boot parameter has been specified then update the just installed
# configuration file template to reflect the options supplied thereby.

# First, we need to determine which file to update. If there's a .rpmnew file
# then update it since a previous configuration file must already have existed.
file="%{_sysconfdir}/brltty.conf"
new="${file}.rpmnew"
[ -f "${new}" ] && file="${new}"

# Update the configuration file template via the Bootdisks/bp2cf script.
# Include it right within this scriptlet so that it needn't be installed.
# Imbed it within a subshell to ensure that it won't impact this scriptlet.
(
	# First, set bp2cf's command line arguments.
	set -- -u -f "${file}"

#!/bin/sh
###############################################################################
# BRLTTY - A background process providing access to the Linux console (when in
#          text mode) for a blind person using a refreshable Braille display.
#
# Copyright (C) 1995-2003 by The BRLTTY Team. All rights reserved.
#
# BRLTTY comes with ABSOLUTELY NO WARRANTY.
#
# This is free software, placed under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation.  Please see the file COPYING for details.
#
# Web Page: http://mielke.cc/brltty/
#
# This software is maintained by Dave Mielke <dave@mielke.cc>.
###############################################################################

# Convert the boot parameter to configuration file directives.
# If /proc is mounted then use the brltty= boot parameter in /proc/cmdline.
# If /proc is not mounted then use the brltty environment variable.
# Invoke with -h for usage information.

programName="${0##*/}"
programMessage()
{
	echo 2>&1 "${programName}: ${1}"
}
syntaxError()
{
	programMessage "${1}"
	exit 2
}
internalError()
{
	programMessage "${1}"
	exit 3
}

configurationFile=""
requestedAction=create
deviceTranslation=none
requestedParameter=""
OPTIND=1
while getopts ":f:cundop:h" option
do
	case "${option}" in
	    f) configurationFile="${OPTARG}";;
	    c) requestedAction=create;;
	    u) requestedAction=update;;
	    n) deviceTranslation=none;;
	    d) deviceTranslation=devfs;;
	    o) deviceTranslation=old;;
	    p) requestedParameter="${OPTARG}";;
	    h)
		cat <<EOF
Usage: ${programName} [option ...]
-f file  The configuration file to create/update.
-c       Create the configuration file (write to stdout if no -f).
-u       Update the configuration file (copying from stdin to stdout if no -f).
-n       Do not translate device paths.
-d       Do old-style to devfs device path translation.
-o       Do devfs to old-style device path translation.
-p [driver][,[device][,[table]]]
         Explicitly specify the boot parameter.
-h       Display this usage summary.
EOF
		exit 0
		;;
	    \?) syntaxError "unknown option: -${OPTARG}";;
	    :) syntaxError "missing value: -${OPTARG}";;
	    *) internalError "unimplemented option: -${option}";;
	esac
done
shift "`expr $OPTIND - 1`"
[ "${#}" -eq 0 ] || syntaxError "too many parameters."

case "${requestedAction}" in
    create)
	putConfigurationLine()
	{
		echo "${1}" || exit 4
	}
	startConfigurationFile()
	{
		[ -n "${configurationFile}" ] && exec >"${configurationFile}"
		putConfigurationLine "`makeHeaderLine Created`"
		putConfigurationLine "`makeParameterLine`"
		putConfigurationLine ""
	}
	putConfigurationDirective()
	{
		putConfigurationLine "${1} ${2}"
	}
	finalizeConfigurationFile()
	{
		:
	}
	;;
    update)
	putSedCommand()
	{
		sedScript="${sedScript}
${1}"
	}
	startConfigurationFile()
	{
		if [ -n "${configurationFile}" ]; then
			[ -e "${configurationFile}" ] || syntaxError "file not found: ${configurationFile}"
			[ -f "${configurationFile}" ] || syntaxError "not a file: ${configurationFile}"
			[ -r "${configurationFile}" ] || syntaxError "file not readable: ${configurationFile}"
			[ -w "${configurationFile}" ] || syntaxError "file not writable: ${configurationFile}"
			outputFile="${configurationFile}.new"
			exec <"${configurationFile}" >"${outputFile}"
		fi
		sedScript=""
		putSedCommand "1i\\
`makeHeaderLine Updated`\\
`makeParameterLine`\\
"
	}
	putConfigurationDirective()
	{
		value="`echo "${2}" | sed -e 's%\\([/\\]\\)%\\\\\\1%g'`"
		putSedCommand "/^ *#\\(${1} .*\\)/s//\\1/"
		putSedCommand "/^ *\\(${1}\\) .*/s//\\1 ${value}/"
	}
	finalizeConfigurationFile()
	{
		sed -e "${sedScript}"
		[ -n "${outputFile}" ] && mv -f "${outputFile}" "${configurationFile}"
	}
	;;
    *) internalError "unimplemented action: ${requestedAction}";;
esac

translateDevice_none()
{
	:
}
translateDevice_devfs()
{
	minor="${device#ttyS}"
	if [ "${minor}" != "${device}" ]; then
		device="tts/${minor}"
		return 0
	fi
	minor="${device#lp}"
	if [ "${minor}" != "${device}" ]; then
		device="printers/${minor}"
		return 0
	fi
	programMessage "unsupported old-style device: ${device}"
}
translateDevice_old()
{
	major="${device%%/*}"
	if [ "${major}" != "${device}" ]; then
		minor="${device#*/}"
		case "${major}" in
		    tts) devfs="ttyS${minor}";;
		    printers) devfs="lp${minor}";;
		esac
	fi
	if [ -n "${devfs}" ]; then
		device="${devfs}"
	else
		programMessage "unsupported devfs device: ${device}"
	fi
}

makeHeaderLine()
{
	echo "# ${1} by brltty-bp2cf`date +' on %Y-%m-%d at %H:%M:%S %Z (UTC%z)'`."
}
makeParameterLine()
{
	echo "# Boot Parameter:${bootParameter}"
}
putConfigurationFile()
{
	startConfigurationFile
	[ -n "${brailleDriver}" ] && putConfigurationDirective "braille-driver" "${brailleDriver}"
	[ -n "${brailleDevice}" ] && {
	device="`echo "${brailleDevice}" | sed -e 's%//*%/%g' -e 's%^/dev/%%'`"
	if [ "${device#/}" = "${device}" ]; then
		translateDevice_${deviceTranslation}
	fi
	putConfigurationDirective "braille-device" "${device}"
	}
	[ -n "${textTable}" ] && putConfigurationDirective "text-table" "${textTable}"
	finalizeConfigurationFile
}
parseBootParameter()
{
	bootParameter="${bootParameter} ${1}"
	number=1
	while [ "${number}" -le 3 ]; do
		cut="cut -d, -f${number}"
		[ "${number}" -gt 1 ] && cut="${cut} -s"
		operand="`echo ${1} | ${cut}`"
		if [ -n "${operand}" ]; then
			case "${number}" in
			    1) brailleDriver="${operand}";;
			    2) brailleDevice="${operand}";;
			    3) textTable="${operand}";;
			esac
		fi
		number="`expr ${number} + 1`"
	done
}
putBootParameter()
{
	parseBootParameter "${1}"
	putConfigurationFile
}
parseBootCommand()
{
	found=false
	while [ "${#}" -gt 0 ]; do
		case "${1}" in
		    "brltty="*)
			found=true
			parseBootParameter "${1#*=}"
			;;
		esac
		shift
	done
	"${found}" && putConfigurationFile
}

brailleDriver=""
brailleDevice=""
textTable=""
bootCommandFile="/proc/cmdline"
if [ -n "${requestedParameter}" ]; then
	putBootParameter "${requestedParameter}"
elif [ -f "${bootCommandFile}" ]; then
	parseBootCommand `cat "${bootCommandFile}"`
elif [ -n "${brltty}" ]; then
	putBootParameter "${brltty}"
fi
exit 0
)

%post	-n brlapi -p /sbin/ldconfig
%postun	-n brlapi -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc Documents/{Manual-BRLTTY/English/BRLTTY*,ChangeLog,HISTORY,TODO}
%attr(755,root,root) %{_bindir}/brltty
%attr(755,root,root) %{_bindir}/brltty-atb
%attr(755,root,root) %{_bindir}/brltty-config
%attr(755,root,root) %{_bindir}/brltty-cldr
%attr(755,root,root) %{_bindir}/brltty-ctb
%attr(755,root,root) %{_bindir}/brltty-ktb
%attr(755,root,root) %{_bindir}/brltty-lscmds
%attr(755,root,root) %{_bindir}/brltty-lsinc
%attr(755,root,root) %{_bindir}/brltty-morse
%attr(755,root,root) %{_bindir}/brltty-trtxt
%attr(755,root,root) %{_bindir}/brltty-ttb
%attr(755,root,root) %{_bindir}/brltty-tune
%attr(755,root,root) %{_bindir}/eutp
%attr(755,root,root) %{_bindir}/vstp
%{?with_x:%attr(755,root,root) %{_bindir}/xbrlapi}
%dir %{_libdir}/brltty
# Braille drivers
%attr(755,root,root) %{_libdir}/brltty/libbrlttybal.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybat.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybba.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbc.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbd.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbg.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbl.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbm.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybbn.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybcb.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybce.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybec.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybeu.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybfs.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybhd.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybhm.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybht.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybhw.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybic.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybir.so
%{?with_libbraille:%attr(755,root,root) %{_libdir}/brltty/libbrlttyblb.so}
%attr(755,root,root) %{_libdir}/brltty/libbrlttyblt.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybmb.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybmd.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybmm.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybmn.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybmt.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybnp.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybpg.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybpm.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybsk.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybtn.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybts.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybtt.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybvd.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybvo.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybvr.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttybvs.so
%{?with_x:%attr(755,root,root) %{_libdir}/brltty/libbrlttybxw.so}
# speech synthesizer drivers
%attr(755,root,root) %{_libdir}/brltty/libbrlttysal.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttysbl.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttyscb.so
%{?with_espeak_ng:%attr(755,root,root) %{_libdir}/brltty/libbrlttysen.so}
%{?with_espeak:%attr(755,root,root) %{_libdir}/brltty/libbrlttyses.so}
%{?with_flite:%attr(755,root,root) %{_libdir}/brltty/libbrlttysfl.so}
%attr(755,root,root) %{_libdir}/brltty/libbrlttysfv.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttysgs.so
%{?with_mikropuhe:%attr(755,root,root) %{_libdir}/brltty/libbrlttysmp.so}
%{?with_speech_dispatcher:%attr(755,root,root) %{_libdir}/brltty/libbrlttyssd.so}
%{?with_swift:%attr(755,root,root) %{_libdir}/brltty/libbrlttyssw.so}
%{?with_theta:%attr(755,root,root) %{_libdir}/brltty/libbrlttysth.so}
%{?with_viavoice:%attr(755,root,root) %{_libdir}/brltty/libbrlttysvv.so}
%attr(755,root,root) %{_libdir}/brltty/libbrlttysxs.so
# screen drivers
%{?with_at_spi2:%attr(755,root,root) %{_libdir}/brltty/libbrlttyxa2.so}
%{?with_at_spi:%attr(755,root,root) %{_libdir}/brltty/libbrlttyxas.so}
%attr(755,root,root) %{_libdir}/brltty/libbrlttyxlx.so
%attr(755,root,root) %{_libdir}/brltty/libbrlttyxsc.so
%{_sysconfdir}/brltty
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/brltty.conf
%{systemdtmpfilesdir}/brltty.conf
%dir /var/lib/BrlAPI
%dir /var/run/brltty
%{_mandir}/man1/brltty.1*
%{_mandir}/man1/eutp.1*
%{_mandir}/man1/vstp.1*
%{?with_x:%{_mandir}/man1/xbrlapi.1*}

%if %{with x}
# gdm autostart - subpackage?
#%{_datadir}/gdm/greeter/autostart/xbrlapi.desktop
#/etc/X11/Xsession.d/60xbrlapi
%{_datadir}/metainfo/org.a11y.brltty.metainfo.xml
%endif
%{_datadir}/polkit-1/actions/org.a11y.brlapi.policy

%files -n brlapi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbrlapi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbrlapi.so.0.7

%files -n brlapi-devel
%defattr(644,root,root,755)
%doc Documents/Manual-BrlAPI/English/BrlAPI*
%attr(755,root,root) %{_libdir}/libbrlapi.so
%{_includedir}/brltty
%{_includedir}/brlapi*.h
%{_mandir}/man3/brlapi_*.3*

%files -n brlapi-static
%defattr(644,root,root,755)
%{_libdir}/libbrlapi.a

%if %{with apidocs}
%files -n brlapi-apidocs
%defattr(644,root,root,755)
%doc Documents/BrlAPIref/html/*
%endif

%if %{with java}
%files -n java-brlapi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/java/libbrlapi_java.so
%{_javadir}/brlapi.jar
%endif

%if %{with ocaml}
%files -n ocaml-brlapi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllbrlapi_stubs.so

%files -n ocaml-brlapi-devel
%defattr(644,root,root,755)
%dir %{_libdir}/ocaml/brlapi
%{_libdir}/ocaml/brlapi/META
%{_libdir}/ocaml/brlapi/brlapi.cm[aix]*
%{_libdir}/ocaml/brlapi/brlapi.mli
%{_libdir}/ocaml/brlapi/libbrlapi_stubs.a
%endif

%if %{with python}
%files -n python-brlapi
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/brlapi.so
%{py_sitedir}/Brlapi-%{brlapi_ver}-py*.egg-info

%if %{with python3}
%files -n python3-brlapi
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/brlapi.cpython-*.so
%{py3_sitedir}/Brlapi-%{brlapi_ver}-py*.egg-info
%endif
%endif

%if %{with tcl}
%files -n brlapi-tcl
%defattr(644,root,root,755)
%dir %{_libdir}/brlapi-%{brlapi_ver}
%attr(755,root,root) %{_libdir}/brlapi-%{brlapi_ver}/libbrlapi_tcl.so
%{_libdir}/brlapi-%{brlapi_ver}/pkgIndex.tcl
%endif
