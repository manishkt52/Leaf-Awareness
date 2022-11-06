import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { IndexComponent } from './index/index.component';
import { DetectComponent } from './detect/detect.component';
//import { HttpClientComponent } from './service/http-client/http-client.component';
import { HttpClientService } from './service/http-client.service';
import { HttpInterceptorService } from './service/http-interceptor.service';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { LearningModuleComponent } from './learning-module/learning-module.component';
import { AddleafComponent } from './addleaf/addleaf.component';
@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    DetectComponent,
    LearningModuleComponent,
    AddleafComponent,
    //HttpClientComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [{ provide: HTTP_INTERCEPTORS, useClass: HttpInterceptorService, multi: true },],
  bootstrap: [AppComponent]
})
export class AppModule { }
