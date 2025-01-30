
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { SustainabilityAction } from '../models/sustainability-action';

@Injectable({
  providedIn: 'root'
})
export class SustainabilityService {
  private apiUrl = 'http://localhost:8000/api/actions/';

  constructor(private http: HttpClient) { }

  getActions(): Observable<SustainabilityAction[]> {
    return this.http.get<SustainabilityAction[]>(this.apiUrl);
  }

  addAction(action: SustainabilityAction): Observable<SustainabilityAction> {
    return this.http.post<SustainabilityAction>(this.apiUrl, action);
  }
}