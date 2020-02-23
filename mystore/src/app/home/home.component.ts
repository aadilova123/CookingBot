import { Component, OnInit } from '@angular/core';
import { Home } from '../home';
import { HOMES } from '../mock-home';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {

  heroes = HOMES;
  selectedHome: Home;

  constructor() { }

  ngOnInit() {
  }

  onSelect(home: Home): void {
    this.selectedHome = home;
  }
}

