import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { CreateGroupComponent } from './create-group/create-group.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'groups', component: CreateGroupComponent },
  { path: 'about', component: AboutComponent }
];

export const routing = RouterModule.forRoot(routes);