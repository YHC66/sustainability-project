import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SustainabilityListComponent } from './components/sustainability-list/sustainability-list.component';

const routes: Routes = [
  { path: '', component: SustainabilityListComponent }  // Default route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }