Name:		dv2sub
Version:	0.3
Release:	%mkrel 1
Summary:	Extracts info or subtitles from DV stream
License:	GPLv2+
Group:		Video
Url:		http://dv2sub.sourceforge.net/
Source0:	http://downloads.sourceforge.net/dv2sub/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	libdv-devel

%description
A simple util that extracts the date and time of recording from a dv video file
(using libdv) and outputs it as a subtitle file.

It can also display useful information about the dv stream, like video norm 
(PAL/NTSC), aspect ratio normal (4:3) or wide (16:9), interlaced or progressive
material, number of audio channels, audio sampling frequency, number of audio 
samples, timestamp and recording date & time.

Be sure the input file or stream is in pure RAW DV format. dv2sub doesn't work
with DV AVI files (type 1 or type 2)

%package kino-scripts
Summary:	Export scripts provided by dv2sub for DV editing tool Kino
Group:		Video

Requires:	dv2sub
Requires:	kino
Requires:	dvdauthor

%description kino-scripts
This package contains export scripts for DV editing tool Kino provided by
dv2sub.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

# install kino scripts and move dv2sub_spumux.xml to include it in doc
install -d -m755 %{buildroot}%{_datadir}/kino/scripts/exports
install -D -m755 kino_scripts/*.sh %{buildroot}%{_datadir}/kino/scripts/exports
install -d -m755 examples
install -D -m644 kino_scripts/%{name}_spumux.xml examples

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO 
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files kino-scripts
%defattr(-,root,root,-)
%doc examples
%{_datadir}/kino/scripts/exports/*.sh
