Name:           alsa-plugins
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  libtool
BuildRequires:  libpulse-devel
BuildRequires:  speex-devel
Url:            http://www.alsa-project.org/
Summary:        Extra Plug-Ins for the ALSA Library
License:        LGPL-2.1+
Group:          System/Libraries
Version:        1.0.26
Release:        0
Source:         ftp://ftp.alsa-project.org/pub/plugins/alsa-plugins-%{version}.tar.bz2
Source1:        asound-pulse.conf
Source2:        alsa-pulse.conf
Source3:        baselibs.conf
Source1001: 	alsa-plugins.manifest

%description
This package contains the extra plug-ins for the ALSA library.

%package pulse
Summary:        Pulseaudio Plug-In for the ALSA Library
License:        GPL-2.0+ and LGPL-2.1+
Group:          System/Libraries
Requires:       pulseaudio

%description pulse
pulseaudio is a networked sound server for Linux and other Unix like
operating systems and Microsoft Windows. It is intended to be an
improved drop-in replacement for the Enlightened Sound Daemon (ESOUND).

This package contains the polypaudio I/O plug-in for the ALSA library.

%package speex
Summary:        Speex Prerocessor Plug-In for the ALSA Library
License:        LGPL-2.1+
Group:          System/Libraries
%description speex
This package contains the Speex preprocessor plugin for the ALSA
library using libspeexdsp.


%prep
%setup -q 
cp %{SOURCE1001} .

%build
export AUTOMAKE_JOBS="%{?_smp_mflags}"
autoreconf -fi
%configure --with-speex=builtin
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}/etc/
%__install -m 0644 %_sourcedir/asound-pulse.conf %{buildroot}/etc/
%__install -m 0644 %_sourcedir/alsa-pulse.conf %{buildroot}/etc/

%post pulse
if type -p setup-pulseaudio > /dev/null; then
    setup-pulseaudio --auto
fi
exit 0

%postun pulse
if type -p setup-pulseaudio > /dev/null; then
    setup-pulseaudio --auto
fi
exit 0

%files
%manifest %{name}.manifest
%defattr(-, root, root)
%license COPYING
%{_libdir}/alsa-lib/libasound_module_ctl_oss.so
%{_libdir}/alsa-lib/libasound_module_pcm_oss.so
%{_libdir}/alsa-lib/libasound_module_pcm_upmix.so
%{_libdir}/alsa-lib/libasound_module_pcm_vdownmix.so
%{_libdir}/alsa-lib/libasound_module_pcm_usb_stream.so
%{_libdir}/alsa-lib/libasound_module_rate_speexrate*.so
%{_libdir}/alsa-lib/libasound_module_ctl_arcam_av.so

%files pulse
%manifest %{name}.manifest
%defattr(-, root, root)
%license COPYING
%{_libdir}/alsa-lib/libasound_module_ctl_pulse.so
%{_libdir}/alsa-lib/libasound_module_pcm_pulse.so
%{_libdir}/alsa-lib/libasound_module_conf_pulse.so
%config /etc/asound-pulse.conf
%config /etc/alsa-pulse.conf
%{_datadir}/alsa/alsa.conf.d

%files speex
%manifest %{name}.manifest
%defattr(-, root, root)
%license COPYING
%{_libdir}/alsa-lib/libasound_module_pcm_speex.so

