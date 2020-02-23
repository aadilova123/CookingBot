import { Component, OnInit } from '@angular/core';
import { Observable, Subject } from 'rxjs';

import { Women } from '../women';
import { WServiceService } from '../wservice.service';


import {
  debounceTime, distinctUntilChanged, switchMap
} from 'rxjs/operators';


@Component({
  selector: 'app-w-search',
  templateUrl: './w-search.component.html',
  styleUrls: ['./w-search.component.css']
})
export class WSearchComponent implements OnInit {

  women$: Observable<Women[]>;
  private searchTerms = new Subject<string>();
  constructor(private Wservice : WServiceService) { }

  search(term: string): void {
    this.searchTerms.next(term);
  }

  ngOnInit(): void {
    this.women$ = this.searchTerms.pipe(
      // wait 300ms after each keystroke before considering the term
      debounceTime(300),

      // ignore new term if same as previous term
      distinctUntilChanged(),

      // switch to new search observable each time the term changes
      switchMap((term: string) => this.Wservice.searchHeroes(term)),
    );

  }

}

