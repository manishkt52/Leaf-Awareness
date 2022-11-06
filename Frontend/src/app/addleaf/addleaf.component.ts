import { Component, OnInit } from '@angular/core';
import { HttpClientService } from '../service/http-client.service';
import {Router} from '@angular/router';
import { User } from '../user';
import { Variable } from '@angular/compiler/src/render3/r3_ast';

var baseData = "";

@Component({
  selector: 'app-addleaf',
  templateUrl: './addleaf.component.html',
  styleUrls: ['./addleaf.component.scss']
})
export class AddleafComponent implements OnInit {
  sendres:any
  srcData:any
  fileToUpload: any
  plantName:any
  userModel=new User('','','');
  constructor(private httpClient:HttpClientService,private router: Router) { 
    
  }

  ngOnInit(): void {
  }

  

  onChange(event: any) {
    console.log(event);
    this.fileToUpload = event.target.files[0];
    
  }
  onChangetext() {
      var x=<HTMLInputElement>document.getElementById('plant');
      this.plantName=x.value;
      console.log(this.plantName);
      this.httpClient.sendimgname(this.plantName).subscribe(
        res=>{
          
        })
    
  }
  
  onsubmit()
   {
      this.httpClient.sendfiledata(this.userModel).subscribe(
        res=>{
        })
        this.httpClient.sendimagedata(this.fileToUpload).subscribe(
          res=>{
            this.sendres=res;
            alert(this.sendres);
          })
   }
  }


