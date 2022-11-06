import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { IndexComponent } from './index/index.component';
import { DetectComponent } from './detect/detect.component';
import { LearningModuleComponent } from './learning-module/learning-module.component';
import { AddleafComponent } from './addleaf/addleaf.component';

const routes: Routes = [
  {path:'index',component:IndexComponent},
  {path:'detect',component:DetectComponent},
  {path:'LearningModule',component:LearningModuleComponent},
  {path:'addleaf',component:AddleafComponent},
  {path:'**',redirectTo:'index'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
