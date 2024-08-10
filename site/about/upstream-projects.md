<div class='status-page'>
  <section class='banner'>
    <div class='containerCustom'>
      <div class='left-shape'>
        <img src='/img/global/shape-left.svg' />
      </div>
      <div class='right-shape'>
        <img src='/img/global/shape-right.svg' />
      </div>

  <div class='banner-div'>


# Upstream projects

  </div>

  </div>
  </section>

  <section class='content-section'>
    <div class='content-div'>


## Debian GNU/Linux

Debian GNU/Linux has been our base distribution for many years.
We use Debian's live-build to build our images, and Debian gives us a stable and reliable
base system to build upon.

### How do we contribute to Debian?

VyOS is a platinum-level sponsor of Debian long-term support project led by [Freexian](https://www.freexian.com/lts/debian/).

## Linux kernel

We are still amazed by networking capabilities of the Linux kernel.
Our firewall and NAT, AH and ESP parts of IPsec, VRF, multi-path routing,
and lots of other things are frontends for features of the kernel — and so is support for
a huge number of network cards and other hardware.

## FreeRangeRouting (FRR)

[FreeRangeRouting](https://frrouting.org) is our routing protocol stack and control plane.
That's what powers our BGP, OSPF, IS-IS, PIM, and other dynamic routing protocols,
maintains a unified <abbr title="Routing Information Base">RIB</abbr>,
and installs routes into the Linux kernel network stack.

FRR is an actively-developed fork of the now-defunct Quagga project that we used previously,
and we are looking forward to many more years of collaboration with its maintainers.

### How do we contribute to FRR?

We sponsor a Slack workspace for the FRR community, and we contribute code
and report bugs to them.

## Python

Our configuration scripts and operational mode commands are written in Python.
We love the design of the language, we adopted Python3 right away, and we make heavy use of
recent features such as gradual typing — for example, our operational mode command options
and API endpoints are automatically generated from function names and their type annotations.

Without a large ecosystem of libraries and long-established projects like the Jinja2 template processor,
those scripts would take a lot longer to write. Another reason we chose Python is that
many systems and network administrators are already familiar with it from automation tools and scripts
and it makes it easier for them to start contributing to VyOS.

### How do we contribute to Python?

We make donations to [Python Software Foundation](https://www.python.org/psf/donations/).

## OCaml

The core parts of the configuration subsystem are written in OCaml — a functional, strict language,
compiled to native machine code. Python modules for working with the configuration tree
are in fact thin wrappers for the OCaml library,
and we will eventually replace the legacy configuration backend completely.

Immutable (persistent) datastructures allow us to work with multiple slightly different copies of a configuration tree
without copying them, and we like how the language is very expressive and fast.

### How do we contribute to OCaml?

Our team members maintain multiple libraries and made contributions to the libraries we use
and some small contributions to the OCaml runtime.

## Accel-PPP

Accel-PPP powers our PPPoE, IPoE, L2TP, SSTP, and PPTP implementations.
Adopting it gave us more protocols and a much better performance
than other alternatives could provide.

## StrongSWAN

StrongSWAN is our <abbr title="Internet Key Exchange">IKE</abbr> implementation.
IPsec traffic encryption is implemented in the Linux kernel,
but it needs an IKE implementation to establish connections with peers
and negotiate settings, and StrongSWAN does that well.

We deeply appreciate that StrongSWAN provides an [API](https://github.com/strongswan/strongswan/blob/master/src/libcharon/plugins/vici/README.md)
and Python libraries for interacting with it — that makes our work a lot easier!

## Kea

CUrrently supported LTS releases (1.4 and 1.3) still use legacy ISC DHCP server,
but rolling release and stream images already use Kea and take advantage of its
many design and implementation improvements.

## Keepalived

We use Keepalived for our VRRP implementation and LVS configuration.

### How do we contribute to Keepalived?

We contributed some improvements to it, including machine-readable statistic output.

## WireGuard

VyOS was one of the first network OSes to add WireGuard to its CLI
and give users an option to use a fast and lightweight VPN protocol
in addition to classics like IPsec and OpenVPN.

### How do we contribute to WireGuard?

We sponsored the maintainer for quite a while.

## OpenVPN

We support OpenVPN in all three modes (server, client, and site-to-site)
and we are happy to integrate all new features its adds,
such as DCO (Data Channel Offload) acceleration
and fingerprint-based site-to-site mode.

## PowerDNS

We use PowerDNS for our DNS forwarding and authoritative DNS services —
it's fast, flexible, and secure.

</div>
</div>
