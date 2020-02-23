// import { NgModule } from '@angular/core';
// import { Routes, RouterModule } from '@angular/router';
// import { WomanComponent }   from './woman/woman.component';
// import { WDetailComponent }  from './w-detail/w-detail.component';


// const routes: Routes = [
//   { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
//   { path: 'Woman', component: WomanComponent },
//   { path: 'w-detail/:id', component: WDetailComponent },
// ];


// @NgModule({
//   imports: [RouterModule.forRoot(routes)],
//   exports: [RouterModule]
// })
// export class AppRoutingModule { }

import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {ProductItemComponent} from './product-item/product-item.component';
import {ProductListComponent} from './product-list/product-list.component';
import {CategoryComponent} from './category/category.component';


const routes: Routes = [
  { path: 'products', component: ProductListComponent},
  { path: '', redirectTo: '/products', pathMatch: 'full'},
  { path: 'product-id/:id', component: ProductItemComponent},
  { path: 'category/:id', component: CategoryComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


