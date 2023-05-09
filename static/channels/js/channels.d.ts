declare module 'static/channels/js/channels' {
  export class WebSocketBridge {
    connect(url: string): void;
    listen(callback: (payload: any) => void): void;
    send(payload: any): void;
  }
}
