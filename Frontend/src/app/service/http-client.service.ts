import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class HttpClientService {
  static sendImageData(userModel: any) {
    throw new Error('Method not implemented.');
  }

  constructor(private httpClient : HttpClient) { }

  getfilename(query: any) {
    return this.httpClient.post<any>(`${environment.apiBaseUrl}/predict`, query);
  }
  sendfiledata(query: any)
  {
    return this.httpClient.post<any>(`${environment.apiBaseUrl}/adddata`, query);
  }
  sendimagedata(query:any)
  {
    return this.httpClient.post<any>(`${environment.apiBaseUrl}/imagedata`, query);
  }
  sendimgname(query:any)
  {
    return this.httpClient.post<any>(`${environment.apiBaseUrl}/imagename`, query);
  }
}
