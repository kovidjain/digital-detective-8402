# Mission 7 — Networking notes

## 1. Clients and servers

A client is a program or device that requests a service. A server is a program or device that listens for requests and provides a resource or result. The roles describe what each side is doing in an exchange, so one computer can act as a client for one service and a server for another.

For a web page request, a browser is the client and a web server provides the page. The client sends a request, and the server sends a response that may contain text, images, scripts, or an error message.

## 2. DNS

The Domain Name System (DNS) translates a human-readable domain name into an address that network software can use. This means a person can enter a name instead of remembering a numeric address.

| DNS step | Purpose |
| --- | --- |
| Client lookup | The application asks a resolver for the address of a domain. |
| Resolver search | The resolver checks its cache or queries other DNS servers. |
| Answer | The resolver returns an address record and a time-to-live value. |
| Connection | The client uses the returned address to contact the service. |

DNS does not deliver the page itself. It helps the client find where the service is available. Cached answers can reduce repeated lookups, but they expire so changes can eventually be noticed.

## 3. Routers and packets

A network message is divided into packets so it can travel through shared networks. A router examines addressing information and forwards each packet toward its destination. Different packets may take different paths and be reassembled or handled by the receiving system.

A router connects networks and makes forwarding decisions. It does not normally need to understand the full meaning of the web page, document, or image inside the packet. Its main job is to move traffic between network segments according to its routing information.

## 4. Protocols

Protocols are agreed rules for formatting, sending, receiving, and interpreting data.

| Protocol or family | Main purpose |
| --- | --- |
| IP | Provides addressing and packet delivery between networks. |
| TCP | Provides an ordered, reliable byte stream between endpoints. |
| UDP | Sends datagrams with less overhead and no guarantee of delivery. |
| DNS | Resolves domain names to network addresses. |
| HTTP | Defines requests and responses for web resources. |
| HTTPS | Uses HTTP with encryption and authentication through TLS. |

Protocols can be layered. For example, an HTTPS request uses an application protocol over a secure connection, which uses a transport protocol, which uses IP for addressing and forwarding.

## 5. Simplified web-request flow

1. I enter a web address in a browser, which identifies the requested service.
2. The browser asks DNS for the address associated with the domain name.
3. The browser opens a connection to the returned address using the required transport and security steps.
4. The browser sends an HTTP request that names the resource it wants.
5. Routers forward packets through several networks toward the server.
6. The server receives the request, processes it, and sends an HTTP response.
7. Packets travel back to the client, where the browser checks and reassembles the data.
8. The browser interprets the response and displays the result.

The exact details vary by protocol, cache state, and network design, but this flow shows how naming, addressing, forwarding, transport, and application messages work together.
